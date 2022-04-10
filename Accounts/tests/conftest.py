import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create(username='testuser')