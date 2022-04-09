from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROFESSION_CHOICES = [
    (1, 'Clinical Research Associate'),
    (2, 'Medical Doctor'),
    (3, 'Pharmacologist'),
    (4, 'EMA officer')
]


class UserExtraInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.SmallIntegerField(choices=PROFESSION_CHOICES)
    site_name = models.CharField(max_length=255)
    site_adress = models.TextField()