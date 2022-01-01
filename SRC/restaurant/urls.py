from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("food-list/", food_list, name="foods_list"),
    path("meal-category-list/", meal_category_list, name="meal_category_list"),
    path("food-restaurant-meal-list/", food_restaurant_meal_list, name="food_restaurant_meal_list"),
    path("restaurant-list/", restaurants_list, name="Restaurants_list"),
    path("branches-list/", branches_list, name="branches_list"),

    path("food-reataurant-meal-foods-list/<int:food_restaurant_category_id>",
         food_reataurant_meal_foods_list, name="food_reataurant_meal_foods_list"),

    path("meal_category_foods_list/<int:meal_category_id>",
         meal_category_foods_list, name="meal_category_foods_list"),

    path("restaurant-branches-list/<int:restaurant_id>",
         restaurant_branches_list, name="restaurant_branches_list"),
]
