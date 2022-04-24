from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Drug(models.Model):
    #dosage in mg units
    name = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=24, unique=True)
    status = models.CharField(max_length=128, unique=True)
    dosage = models.FloatField()

    def __str__(self):
        return self.label

class StudyScheme(models.Model):
    name = models.CharField(max_length=64)
    patient_cohort = models.SmallIntegerField(default=20)
    therapy_duration = models.SmallIntegerField(default=70)
    visits_frequency = models.SmallIntegerField(default=14)

    def __str__(self):
        return self.name

class Patients(models.Model):
    sex_types = (
        ('M', 'male'),
        ('F', 'female')
    )
    race_and_ethnicity_types = (
        (0, 'Asian'),
        (1,'American Indian or Alaska Nativ'),
        (2, 'Black or African American'),
        (3, 'Hispanic or Latino'),
        (4, 'Native Hawaiian or Other Pacific Islander'),
        (5, 'White'),
    )
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    age = models.SmallIntegerField()
    sex = models.CharField(choices=sex_types, max_length=3)
    race_and_ethnicity = models.SmallIntegerField(choices=race_and_ethnicity_types)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, null=True)
    study_scheme = models.ForeignKey(StudyScheme, on_delete=models.CASCADE)
    patient_author = models.ForeignKey(User, on_delete=models.PROTECT)


class AdverseEvent(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    onset = models.DateField()
    end = models.DateField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

class Visit(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()
    ogtt = models.FloatField()
    discontinuation = models.BooleanField(default=False)
    related_adverse_event = models.OneToOneField(AdverseEvent, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name