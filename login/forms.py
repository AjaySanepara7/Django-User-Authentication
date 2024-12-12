from django import forms
from login.models import Person
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id": "password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control border border-2 border-dark", "placeholder": "Username"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control border border-2 border-dark", "placeholder": "First Name"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control border border-2 border-dark", "placeholder": "Last Name"})
        self.fields["email"].widget.attrs.update({"class": "form-control border border-2 border-dark", "placeholder": "Email"})
        self.fields["password"].widget.attrs.update({"class": "form-control border border-2 border-dark", "placeholder": "Password"})
        self.fields["confirm_password"].widget.attrs.update({"class": "form-control border border-2 border-dark", "placeholder": "Confirm Password"})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']


class PersonForm(forms.ModelForm):
    person_gender = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others")
    ]
    hobbies = [
        ("S", "Sports"),
        ("T", "Travelling"),
        ("R", "Reading"),
        ("P", "Painting"),
        ("w", "Writing")
    ]
    gender = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = person_gender
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control border border-2 border-dark", "name": "date_of_birth", "type": "date"}) 
    )
    hobby = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(attrs={"name": "hobby"}),
        choices = hobbies
    )

    class Meta:
        model = Person
        fields = ['gender', 'date_of_birth', 'hobby', 'profie_picture']