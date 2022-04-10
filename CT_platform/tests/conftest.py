import pytest
from CT_platform.models import Drug, StudyScheme
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
def drug():
    return Drug.objects.create(
        name='drug', label='drugA', status='placebo',
        dosage=1.5)

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
def study_scheme():
    return StudyScheme.objects.create(
            patient_cohort=10, therapy_duration=50, visits_frequency=14)

@pytest.fixture
def study_schemes():
    study_schemes = []
    for scheme in range(5):
        ss = StudyScheme.objects.create(
            patient_cohort=scheme, therapy_duration=scheme, visits_frequency=scheme)
        study_schemes.append(ss)
    return study_schemes

