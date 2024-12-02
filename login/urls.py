from django.urls import path
from login import views


app_name = "login"
urlpatterns = [
    path("", views.home, name="home"),
    path("login_page/", views.login_page, name="login_page"),
    path("successful_login/", views.successful_login, name="successful_login"),
    path("register/", views.registration, name="registration"),
    path("forget_password_page/", views.forget_password_page, name="forget_password_page"),
]