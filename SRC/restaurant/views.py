from django.shortcuts import render
from django.views.generic import DetailView

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


class FoodRestaurantCategoryDetail(DetailView):
    model = FoodRestaurantCategory
    template_name = "restaurant/food_reataurant_meal_foods_list.html"

    def get_context_data(self, *args, **kwargs):
        frc = FoodRestaurantCategory.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.filter(food_restaurant_category=frc)
        return context


def meal_category_foods_list(request, meal_category_id):
    meal_category = MealCategory.objects.get(id=meal_category_id)
    data = Food.objects.filter(meal_category=meal_category).order_by("-id")
    return render(request, "restaurant/meal_category_foods_list.html", {"data": data})


def restaurant_branches_list(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    data = Branch.objects.filter(restaurant=restaurant)
    return render(request, "restaurant/restaurant_branches_list.html", {"data": data})


class FoodDetail(DetailView):
    model = Food
    template_name = "restaurant/food_detail.html"


def branch_detail(request, id):
    branch = Branch.objects.get(id=id)
    menus = Menu.objects.filter(branch=branch)
    return render(request, "restaurant/branch_detail.html", {"data": branch, "menus": menus})
