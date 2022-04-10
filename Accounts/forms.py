from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginFormView(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Login'}),
                               label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label="")


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        data = super().clean()
        if data['password'] != data['repeat_password']:
            raise ValidationError("Password error")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


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
        data = super().clean()
        if data['new_password'] != data['repeat_new_password']:
            raise ValidationError("Password error")

    class Meta:
        model = User
        include = ['password']