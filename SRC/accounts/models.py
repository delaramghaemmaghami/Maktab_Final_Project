from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAddress(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return str(self.id)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_address = models.ManyToManyField(UserAddress)


class Customer(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Staff(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "مدیر رستوران"
        verbose_name_plural = "مدیر های رستوران"


class Admin(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "مدیر سایت"
        verbose_name_plural = "مدیران سایت"
