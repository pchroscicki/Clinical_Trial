from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

# Create your tests here.
from CT_platform.models import Drug


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