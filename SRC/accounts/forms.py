from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms
from django.db import transaction


class CustomerCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    # addresses = forms.ModelMultipleChoiceField(
    #     queryset=UserAddress.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        # user.user_address = self.cleaned_data.get("addresses")
        # user.is_customer = True
        user.save()
        return user


class StaffCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        user.is_staff = True
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter your email ...", "id": "hello"}),
        label="Email / Username")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter password ...",
            "id": "hi",
        }
    ))
