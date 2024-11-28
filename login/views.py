from django.shortcuts import render
from .models import Person
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


def home(request):
    return render(request, "login/home.html")


# import pdb; pdb.set_trace()
def login_page(request):
    if request.method == "POST":
        if 'submit' in request.POST:
            user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("login:successful_login"))
            else:
                return HttpResponseRedirect(reverse("login:failed_login"))
        if 'forget_password' in request.POST:
            return HttpResponseRedirect(reverse("login:forget_password_page"))

    return render(request, "login/login_page.html")

@login_required
def successful_login(request):
    return render(request, "login/successful_login.html")


def failed_login(request):
    return render(request, "login/failed_login.html")


def logout_page(request):
    logout(request)
    return render(request, "login/logout_page.html")


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        hobby = request.POST.get("hobby")
        date = datetime.date.today()

        user_1 = User.objects.create_user(username=username, email=email, password=password)
        user_1.save()

        person1 = Person(user=user_1, gender=gender, hobby=hobby, date_of_birth=date)
        person1.save()
    return render(request, "login/registration.html")

def forget_password_page(request):
    if request.method == "POST":
        u = User.objects.get(username= request.POST.get("username"))
        if u is not None:
            u.set_password(request.POST.get("new_password"))
            u.save()
            return HttpResponseRedirect(reverse("login:success_change_password"))
        else:
            return HttpResponseRedirect(reverse("login:fail_change_password"))
    return render(request, "login/forget_password_page.html")


def success_change_password(request):
    return render(request, "login/success_change_password.html")


def fail_change_password(request):
    return render(request, "login/fail_change_password.html")