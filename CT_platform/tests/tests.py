import datetime

from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

# Create your tests here.
from CT_platform.models import Drug, StudyScheme, Patients, Visit, AdverseEvent


def test_empty():
    assert True

@pytest.mark.config
def test_to_be_OK():
    assert 2 + 2 == 4

@pytest.mark.views
def test_check_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_drug_view(user):
    url = reverse('add_drug')
    client = Client()
    client.force_login(user)
    d = {
        'name': 'pavulon',
        'label': 'drugA',
        'status': 'reference',
        'dosage': 300.50,
    }
    response = client.post(url, d)
    assert response.status_code == 302
    assert Drug.objects.get(name='pavulon')

@pytest.mark.django_db
def test_drugs_list(user, drugs):
    client = Client()
    client.force_login(user)
    url = reverse('drug_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['drug_list'].count() == len(drugs)
    for drug in drugs:
        assert drug in response.context['drug_list']

@pytest.mark.django_db
def test_add_study_scheme_view(user):
    url = reverse('add_study_scheme')
    client = Client()
    client.force_login(user)
    d = {
        'name': 'A',
        'patient_cohort': 20,
        'therapy_duration': 70,
        'visits_frequency': 14,
        }
    response = client.post(url, d)
    assert response.status_code == 302
    assert StudyScheme.objects.get(id=1)

@pytest.mark.django_db
def test_study_scheme_list(user, study_schemes):
    client = Client()
    client.force_login(user)
    url = reverse('study_scheme_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['study_scheme_list'].count() == len(study_schemes)
    for item in study_schemes:
        assert item in response.context['study_scheme_list']

@pytest.mark.django_db
def test_add_patient_view(user, study_scheme):
    url = reverse('add_patient')
    client = Client()
    client.force_login(user)
    d = {
        'name': 'John',
        'surname': 'Snow',
        'age':  42,
        'sex': 'M',
        'race_and_ethnicity': 5,
        'study_scheme': study_scheme.id
    }
    response = client.post(url, d)
    assert response.status_code == 302
    assert Patients.objects.get(name='John')

@pytest.mark.django_db
def test_patients_list(user, patients, study_scheme, drug):
    client = Client()
    client.force_login(user)
    url = reverse('main_page')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['patients_list'].count() == len(patients)
    for patient in patients:
        assert patient in response.context['patients_list']

@pytest.mark.django_db
def test_patient_details_patient(user, patient, adverse_events, visit):
    client = Client()
    client.force_login(user)
    url = reverse('patient_details', kwargs={'patient_id': patient.id})
    response = client.get(url)
    assert response.status_code == 200
    assert patient == response.context['patient']

@pytest.mark.django_db
def test_patient_details_ae(user, patient, adverse_events, visit):
    client = Client()
    client.force_login(user)
    url = reverse('patient_details', kwargs={'patient_id': patient.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['adverse_events'].count() == len(adverse_events)
    for event in adverse_events:
        assert event in response.context['adverse_events']

@pytest.mark.django_db
def test_patient_details_visits(user, patient, adverse_event, visits):
    client = Client()
    client.force_login(user)
    url = reverse('patient_details', kwargs={'patient_id': patient.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['visits'].count() == len(visits)
    for visit in visits:
        assert visit in response.context['visits']

@pytest.mark.django_db
def test_patient_details_ae_order(user, patient, adverse_events, visit):
    primary_list = AdverseEvent.objects.all().values_list('id')
    print(primary_list)
    client = Client()
    client.force_login(user)
    url = reverse('patient_details', kwargs={'patient_id': patient.id})
    response = client.get(url)
    ae_number = len(adverse_events)
    ae_id_order = []
    for x in range(ae_number):
        ae_id_order.append(response.context['adverse_events'][x].id)
    print(ae_id_order)
    for z in range(4):
        assert ae_id_order[z] < ae_id_order[z+1]

@pytest.mark.django_db
def test_add_visit_view(user, patient):
    url = reverse('add_visit', kwargs={'patient_id': patient.id})
    client = Client()
    client.force_login(user)
    d = {
        'weight': 80,
        'ogtt': 23.3,
    }
    response = client.post(url, d)
    assert response.status_code == 302
    assert Visit.objects.get(name='Visit 0')

@pytest.mark.django_db
def test_add_adverse_event(user, patient):
    url = reverse('add_ae', kwargs={'patient_id': patient.id})
    client = Client()
    client.force_login(user)
    today = datetime.date.today()
    d = {
        'name': 'Fever',
        'onset': today,
    }
    response = client.post(url, d)
    assert response.status_code == 302
    assert AdverseEvent.objects.get(name='Fever')

@pytest.mark.django_db
def test_update_adverse_event(user, patient, adverse_event):
    print(adverse_event.name)
    url = reverse('update_ae', kwargs={'patient_id': patient.id, 'ae_id': adverse_event.id})
    client = Client()
    client.force_login(user)
    d = {
        'name': 'Anemia',
        'description': adverse_event.description,
        'onset': adverse_event.onset
    }
    response = client.post(url, d)
    assert response.status_code == 302
    assert AdverseEvent.objects.get(name='Anemia')

