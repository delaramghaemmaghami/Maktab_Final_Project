from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("food-list/", food_list, name="foods_list"),
    path("meal-category-list/", meal_category_list, name="meal_category_list")
]
