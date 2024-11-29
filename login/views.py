from django.shortcuts import render
from login.models import Person
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


def home(request):
    return render(request, "login/home.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            user_person = user.person_set.first()

            return HttpResponseRedirect(reverse("login:successful_login"))
        else:
            return HttpResponseRedirect(reverse("login:failed_login"))

    return render(request, "login/login_page.html")


@login_required
def successful_login(request):
    context = {
        "user": request.user,
        "user_person": request.user.person_set.first()
    }
   
    return render(request, "login/successful_login.html", context)


def failed_login(request):
    return render(request, "login/failed_login.html")


def logout_page(request):
    logout(request)
    return render(request, "login/logout_page.html")

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        date = request.POST.get("date_of_birth")

        if User.objects.filter(username = request.POST.get("username")).exists():
            return HttpResponseRedirect(reverse("login:user_already_exists"))
        else:
            user_1 = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
            user_1.save()
            person1 = Person(user=user_1, gender=gender, hobby=hobby, date_of_birth=date)
            person1.save()
            return HttpResponseRedirect(reverse("login:registration_successful"))
        
    return render(request, "login/registration.html")


def forget_password_page(request):
    if request.method == "POST":
        try:
            u = User.objects.get(username= request.POST.get("username"))
            if u.check_password(request.POST.get("current_password")):
                u.set_password(request.POST.get("password"))
                u.save()
                return HttpResponseRedirect(reverse("login:success_change_password"))
            else:
                return HttpResponseRedirect(reverse("login:fail_change_password"))                
        except:
            return HttpResponseRedirect(reverse("login:fail_change_password"))
    return render(request, "login/forget_password_page.html")


def success_change_password(request):
    return render(request, "login/success_change_password.html")


def fail_change_password(request):
    return render(request, "login/fail_change_password.html")


def user_already_exists(request):
    return render(request, "login/user_already_exists.html")


def registration_successful(request):
    return render(request, "login/registration_successful.html")