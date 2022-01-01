from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "home.html")


def food_list(request):
    data = Food.objects.all().order_by("-id")
    return render(request, "restaurant/food_list.html", {"data": data})


def food_restaurant_meal_list(request):
    data = FoodRestaurantCategory.objects.all().order_by("-id")
    return render(request, "restaurant/food_reataurant_meal_list.html", {"data": data})


def meal_category_list(request):
    data = MealCategory.objects.all().order_by("-id")
    return render(request, "restaurant/meal_category_list.html", {"data": data})


def restaurants_list(request):
    data = Restaurant.objects.all().order_by("-id")
    return render(request, "restaurant/restaurant_list.html", {"data": data})


def branches_list(request):
    data = Branch.objects.all().order_by("-id")
    return render(request, "restaurant/branches_list.html", {"data": data})


def food_reataurant_meal_foods_list(request, food_restaurant_category_id):
    food_restaurant_category = FoodRestaurantCategory.objects.get(id=food_restaurant_category_id)
    data = Food.objects.filter(food_restaurant_category=food_restaurant_category).order_by("-id")
    return render(request, "restaurant/food_reataurant_meal_foods_list.html", {"data": data})


# 'food list' according to 'meal cat'
def meal_category_foods_list(request, meal_category_id):
    meal_category = MealCategory.objects.get(id=meal_category_id)
    data = Food.objects.filter(meal_category=meal_category).order_by("-id")
    return render(request, "restaurant/meal_category_foods_list.html", {"data": data})
