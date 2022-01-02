from django.urls import path
from .views import *
from django.contrib.auth import views


urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("signup/customer/", CustomerSignUpView.as_view(), name="customer_signup"),
    path("signup/staff/", StaffSignUpView.as_view(), name="staff_signup"),
    path('login/',
         views.LoginView.as_view(template_name="accounts/login.html", authentication_form=UserLoginForm),
         name="login")
]
