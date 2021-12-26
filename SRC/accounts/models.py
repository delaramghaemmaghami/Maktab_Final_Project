from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_address = models.CharField(max_length=500, blank=True)  # todo: foreign key


class Customer(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Staff(CustomUser):
    class Meta:
        proxy = True
        verbose_name= "مدیر رستوران"
        verbose_name_plural = "مدیر های رستوران"


class Admin(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "مدیر سایت"
        verbose_name_plural = "مدیران سایت"
