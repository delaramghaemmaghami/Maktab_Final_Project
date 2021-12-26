from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "is_staff", "is_superuser"]
    fieldsets = (
        (None, {"fields": ("first_name", "last_name",)}),
        ("Contact", {"fields": ("email", "user_address",)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Customer)
class CustomerProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff']
    list_display_links = ['id']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
        return Customer.objects.filter(is_staff=False)


@admin.register(Staff)
class StaffProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff', 'is_superuser']
    list_display_links = ['id']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
        return Staff.objects.filter(is_staff=True, is_superuser=False)


@admin.register(Admin)
class AdminProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'is_staff', 'is_superuser']
    list_display_links = ['id']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
        return Admin.objects.filter(is_superuser=True)
