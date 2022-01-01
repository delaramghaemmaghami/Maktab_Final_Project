from django.contrib.auth.forms import UserCreationForm
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
        user.is_customer = True
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
