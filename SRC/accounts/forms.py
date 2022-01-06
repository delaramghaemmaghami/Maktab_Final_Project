from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms
from django.db import transaction


class CustomerCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=15, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        user.device = self.cookie.get("device")
        user.save()

        address = UserAddress.objects.create(city=self.cleaned_data.get("city"),
                                             address=self.cleaned_data.get("address"),
                                             zip_code=self.cleaned_data.get("zip_code"))

        user.user_address.add(address)

        return user

    def __init__(self, *args, **kwargs):
        super(CustomerCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['zip_code'].widget.attrs['class'] = 'form-control'


class StaffCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=15, required=True)

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

        address = UserAddress.objects.create(city=self.cleaned_data.get("city"),
                                             address=self.cleaned_data.get("address"),
                                             zip_code=self.cleaned_data.get("zip_code"))

        user.user_address.add(address)

        return user

    def __init__(self, *args, **kwargs):
        super(StaffCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['zip_code'].widget.attrs['class'] = 'form-control'


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
