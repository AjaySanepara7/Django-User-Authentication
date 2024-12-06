from django import forms
from login.models import Person
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['gender', 'date_of_birth', 'hobby']