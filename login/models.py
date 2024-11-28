from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    
    person_gender = [
        ("M", "Male"),
        ("F", "Female"),
        ("o", "Others")
    ]

    hobbies = [
        ("S", "Swimming"),
        ("R", "Reading"),
        ("T", "Travelling"),
        ("W", "Writing"),
        ("P", "Painting")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, choices=person_gender)
    date_of_birth = models.DateField()
    hobby = models.CharField(max_length=100, choices=hobbies)


    def __str__(self):
        return self.user.username
 