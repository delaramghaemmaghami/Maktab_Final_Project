from django.urls import path, include
from rest_framework import routers

from .views import *


router_one = routers.DefaultRouter()
router_one.register(r"FoodAdminViewSet", FoodAdminViewSet)

router_two = routers.DefaultRouter()
router_two.register(r"FoodCategoryViewSet", FoodCategoryViewSet)

router_three = routers.DefaultRouter()
router_three.register(r"MealViewSet", MealViewSet)


urlpatterns = [
    path("", home, name="home"),

    path("food-list/", food_list, name="foods_list"),
    path("meal-category-list/", meal_category_list, name="meal_category_list"),
    path("food-restaurant-meal-list/", food_restaurant_meal_list, name="food_restaurant_meal_list"),
    path("restaurant-list/", restaurants_list, name="Restaurants_list"),
    path("branches-list/", branches_list, name="branches_list"),

    path("food-reataurant-meal-foods-list/<int:pk>",
         FoodRestaurantCategoryDetail.as_view(), name="food_reataurant_meal_foods_list"),

    path("meal_category_foods_list/<int:meal_category_id>",
         meal_category_foods_list, name="meal_category_foods_list"),

    path("restaurant-branches-list/<int:restaurant_id>",
         restaurant_branches_list, name="restaurant_branches_list"),

    path("food-detail/<int:pk>/", FoodDetail.as_view(), name="food-detail"),
    path("branch-detail/<int:id>/", branch_detail, name="branch-detail"),

    path("admin-panel/", AdminPanel.as_view(), name="admin_panel"),
    path("orders-list/", orders_list, name="orders_list"),

    path("", include(router_one.urls)),
    path("", include(router_two.urls)),
    path("", include(router_three.urls)),

    # path("update-item/", update_item, name="update_item"),
]
