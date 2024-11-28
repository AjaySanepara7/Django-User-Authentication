from django.urls import path
from . import views


app_name = "login"
urlpatterns = [
    path("", views.home, name="home"),
    path("login_page/", views.login_page, name="login_page"),
    path("successful_login/", views.successful_login, name="successful_login"),
    path("failed_login/", views.failed_login, name="failed_login"),
    path("register/", views.registration, name="registration"),
    path("logout_page", views.logout_page, name="logout_page"),
    path("forget_password_page", views.forget_password_page, name="forget_password_page"),
    path("success_change_password", views.success_change_password, name="success_change_password"),
    path("fail_change_password", views.fail_change_password, name="fail_change_password"),
]