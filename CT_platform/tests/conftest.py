import pytest
from CT_platform.models import Drug
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create(username='testuser')

@pytest.fixture
def users():
    users = []
    for x in range(5):
        username=f'{x}'
        u = User.objects.create(username=username)
        users.append(u)
    return users


@pytest.fixture
def drugs():
    drugs = []
    for x in range(5):
        unique_phrase = f'drug_{x}'
        d = Drug.objects.create(
        name=unique_phrase, label=unique_phrase,
        status=unique_phrase, dosage=1.5)
        drugs.append(d)
    return drugs

@pytest.fixture
def drug():
    return Drug.objects.create(
        name='drug', label='drugA', status='placebo',
        dosage=1.5)



