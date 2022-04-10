import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client


def test_to_be_positive():
    assert 2 == 2

@pytest.mark.django_db
def test_register_user(user):
    url = reverse('register')
    client = Client()
    client.force_login(user)
    d = {
        'username':'jlemon',
        'password':'LoveIt',
        'repeat_password': 'LoveIt',
        'first_name': 'John',
        'last_name': 'Lemon',
        'email': 'johnlemon@test.eu'
    }
    response = client.post(url, d)
    assert  response.status_code == 302
    User.objects.get(username='jlemon')
    assert client.login(username='jlemon', password='LoveIt')