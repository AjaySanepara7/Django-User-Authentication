from django.shortcuts import render
from .models import Person
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "login/home.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return render(request, "login/successful_login.html")
        else:
            return render(request, "login/failed_login.html")

    return render(request, "login/login_page.html")


def logout_page(request):
    logout(request)
    return render(request, "login/logout_page.html")

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        hobby = request.POST.get("hobby")
        date = datetime.date.today()

        user_1 = User.objects.create_user(username=username, password=password)
        user_1.save()

        person1 = Person(user=user_1, gender=gender, hobby=hobby, date_of_birth=date)
        person1.save()
    return render(request, "login/registration.html")