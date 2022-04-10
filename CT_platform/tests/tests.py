from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

# Create your tests here.
from CT_platform.models import Drug, StudyScheme


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