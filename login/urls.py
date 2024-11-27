from django.urls import path
from . import views


app_name = "login"
urlpatterns = [
    path("", views.home, name="home"),
    path("login_page/", views.login_page, name="login_page"),
    path("register/", views.registration, name="registration"),
    path("logout_page", views.logout_page, name="logout_page")
]