from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth import views
from .forms import *
from .models import *


def sign_up(request):
    return render(request, "accounts/signup.html")


class CustomerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomerCreationForm
    template_name = "accounts/signup_user.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "customer"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class StaffSignUpView(CreateView):
    model = CustomUser
    form_class = StaffCreationForm
    template_name = "accounts/signup_user.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "staff"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
    

class LoginView(views.LoginView):
    form_class = UserLoginForm
    template_name = "accounts/login.html"
