from django import forms
from django.core.exceptions import ValidationError

from CT_platform.models import Drug

class AddDrugForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = '__all__'


