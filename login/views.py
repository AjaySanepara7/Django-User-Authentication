from django.urls import reverse
from django.conf import settings
from login.models import Person
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "login/home.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("login:successful_login"))
        else:
            context = {
                "login_failed": "Login failed. Invalid credentials"
            }
            return render(request, "login/login_page.html", context)

    return render(request, "login/login_page.html")


@login_required
def successful_login(request):
    context = {
        "user": request.user,
        "user_person": request.user.person_set.first()
    }
    if request.method == "POST":
        logout(request)
        context = {
                "logout": "Logout Successful"
            }
        return render(request, "login/login_page.html", context)
   
    return render(request, "login/successful_login.html", context)


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
            context = {
                "userexists": "User already exists. Username should be unique"
            }
            return render(request, "login/registration.html", context)
        else:
            user_1 = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
            user_1.save()
            person1 = Person(user=user_1, gender=gender, hobby=hobby, date_of_birth=date)
            person1.save()
            context = {
                "registration_success": "Registration Successful"
            }

            return HttpResponseRedirect(reverse("login:login_page"))
        
    return render(request, "login/registration.html")


def forget_password_page(request):
    if request.method == "POST":
        user = request.user
        if user.check_password(request.POST.get("current_password")):
            if user.check_password(request.POST.get("password")):
                context = {
                "same_password": "The new password cannot be the same as the current password"
                }
                return render(request, "login/forget_password_page.html", context)
            else:
                user.set_password(request.POST.get("password"))
                user.save()
                context = {
                "success_change_password": "Password changed successfully"
                }
                return render(request, "login/forget_password_page.html", context)
        else:
            context = {
            "fail_change_password": "Invalid Password"
            }
            return render(request, "login/forget_password_page.html", context)                
    return render(request, "login/forget_password_page.html")