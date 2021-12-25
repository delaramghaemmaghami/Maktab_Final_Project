from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *


class CustomUserAdmin(UserAdmin):
    # fields = ["first_name", "last_name", "username", "email", "is_staff", "is_superuser", "address"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "is_staff", "is_superuser"]
    # readonly_fields = ["email"]
    fieldsets = (
        (None, {"fields": ("first_name", "last_name",)}),
        ("Contact", {"fields": ("email", "user_address",)}),
    )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {"fields": ("first_name", "last_name",)}),
    #     ("Contact", {"fields": ("email", "user_address",)}),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
