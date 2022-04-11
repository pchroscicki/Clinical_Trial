from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from CT_platform.models import Drug, StudyScheme, Patients, Visit, AdverseEvent


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

class AddAdverseEventForm(forms.ModelForm):

    class Meta:
        model = AdverseEvent
        exclude = ['patient', 'author']
        required = ('name', 'onset')
        widgets = {
            'description': forms.Textarea,
            'onset': forms.SelectDateWidget,
            'end': forms.SelectDateWidget,
        }


class AddVisitForm(forms.Form):
    weight = forms.FloatField()
    ogtt = forms.FloatField()
    discontinuation = forms.BooleanField(required=False, initial=False)
    related_adverse_event = forms.ModelChoiceField(queryset=AdverseEvent.objects.all(), required=False, initial=False)



