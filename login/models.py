from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Person(models.Model):
    
    person_gender = [
        ("M", "Male"),
        ("F", "Female"),
        ("o", "Others")
    ]

    hobbies = [
        ("S", "Sports"),
        ("T", "Travelling"),
        ("R", "Reading"),
        ("P", "Painting"),
        ("w", "Writing")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, choices=person_gender)
    date_of_birth = models.DateField()
    hobby = MultiSelectField(choices=hobbies)


    def __str__(self):
        return self.user.username
 