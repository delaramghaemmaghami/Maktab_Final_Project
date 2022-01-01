from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("food-list/", food_list, name="foods_list"),
    path("meal-category-list/", meal_category_list, name="meal_category_list"),
    path("food-restaurant-meal-list/", food_restaurant_meal_list, name="food_restaurant_meal_list")
]
