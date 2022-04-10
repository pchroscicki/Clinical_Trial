from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

# Create your tests here.
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