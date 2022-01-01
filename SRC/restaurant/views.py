from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "home.html")


def meal_category_list(request):
    data = MealCategory.objects.all().order_by("-id")
    return render(request, "restaurant/meal_category_list.html", {"data": data})
