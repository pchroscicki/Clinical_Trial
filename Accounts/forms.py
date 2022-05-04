from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginFormView(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class CreateUserForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['repeat_password']:
            raise ValidationError("Passwords do not match.")


class UserPermUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['groups']
        widgets = {
            'group':forms.CheckboxSelectMultiple
        }

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput())
    repeat_new_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['new_password'] != cleaned_data['repeat_new_password']:
            raise ValidationError("Passwords do not match.")