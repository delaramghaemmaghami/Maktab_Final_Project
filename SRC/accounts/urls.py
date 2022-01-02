from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("signup/customer/", CustomerSignUpView.as_view(), name="customer_signup"),
    path("signup/staff/", StaffSignUpView.as_view(), name="staff_signup"),
    path("login/", LoginView.as_view(), name="login")
]
