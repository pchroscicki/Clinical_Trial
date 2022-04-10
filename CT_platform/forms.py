from django import forms
from django.core.exceptions import ValidationError

from CT_platform.models import Drug, StudyScheme, Patients


class AddDrugForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = '__all__'

class AddStudySchemeForm(forms.ModelForm):

    class Meta:
        model = StudyScheme
        fields = '__all__'

class AddPatientForm(forms.ModelForm):

    class Meta:
        model = Patients
        exclude = ['patient_author', 'drug']



