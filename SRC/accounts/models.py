from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAddress(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=15, blank=True)
    is_main = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return str(self.id)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    user_address = models.ManyToManyField(UserAddress)


class Customer(CustomUser):
    def save(self, *args, **kwargs):
        if not self.id:
            self.is_staff = False
            self.is_superuser = False
            return super(Customer, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Staff(CustomUser):
    def save(self, *args, **kwargs):
        if not self.id:
            self.is_staff = True
            self.is_superuser = False
            return super(Staff, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "مدیر رستوران"
        verbose_name_plural = "مدیر های رستوران"


class Admin(CustomUser):
    def save(self, *args, **kwargs):
        if not self.id:
            self.is_superuser = True
            return super(Admin, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "مدیر سایت"
        verbose_name_plural = "مدیران سایت"
