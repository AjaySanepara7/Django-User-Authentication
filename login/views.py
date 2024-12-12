from django.urls import reverse
from django.conf import settings
from login.models import Person
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from login.forms import UserForm, PersonForm
from django.views import View


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login/home.html")
    

class Registration(View):
    user_form_class = UserForm
    person_form_class = PersonForm
    template_name = "login/registration.html"

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class()
        person_form = self.person_form_class()
        return render(request, self.template_name, {"user_form": user_form, "person_form": person_form})
    
    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.POST)
        person_form = self.person_form_class(request.POST, request.FILES)
        if user_form.is_valid() and person_form.is_valid():
            user_1 = user_form.save()

            person_1 = person_form.save(commit=False)
            person_1.user = user_1
            person_1.save()
            return HttpResponseRedirect(reverse("login:login_page"))
        
        return render(request, self.template_name, {"user_form": user_form, "person_form": person_form})


class LoginPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login/login_page.html")
    
    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("login:successful_login"))
        else:
            context = {
                "login_failed": "Login failed. Invalid credentials"
            }
            return render(request, "login/login_page.html", context)


class SuccessfulLoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "user": request.user,
            "user_person": request.user.person_set.first()
        }
        return render(request, "login/successful_login.html", context)
    
    def post(self, request, *args, **kwargs):
        logout(request)
        context = {
                "logout": "Logout Successful"
            }
        return render(request, "login/login_page.html", context)


class ForgetPasswordView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login/forget_password_page.html")
    
    def post(self, request, *args, **kwargs):
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