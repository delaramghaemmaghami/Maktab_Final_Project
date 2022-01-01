from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "home.html")


def food_list(request):
    data = Food.objects.all().order_by("-id")
    return render(request, "restaurant/food_list.html", {"data": data})


def meal_category_list(request):
    data = MealCategory.objects.all().order_by("-id")
    return render(request, "restaurant/meal_category_list.html", {"data": data})
