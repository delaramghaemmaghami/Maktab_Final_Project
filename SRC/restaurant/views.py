from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, TemplateView
from .models import *
from .forms import *
from accounts.mixins import StaffRequiredMixin, SuperUserRequiredMixin
from .serializer import *
from rest_framework import viewsets, permissions
import json


def home(request):
    foods = Food.objects.all()

    food_total_order = {}

    for food in foods:
        total_order = 0
        menu_orders = MenuOrder.objects.filter(
            Q(order__status="ثبت") | Q(order__status='ارسال') | Q(order__status='تحویل'))

        for mo in menu_orders:
            if mo.menu.food == food:
                total_order += mo.number

        if total_order != 0:
            food_total_order[food] = total_order

    best_sold_foods = dict(sorted(food_total_order.items(), key=lambda x: x[1], reverse=True))

    branches = Branch.objects.all()

    branches_total_order = {}

    for branch in branches:
        total_order = 0
        menu_orders = MenuOrder.objects.filter(
            Q(order__status="ثبت") | Q(order__status='ارسال') | Q(order__status='تحویل'))

        for mo in menu_orders:
            if mo.order.branch == branch:
                total_order += mo.number

        if total_order != 0:
            branches_total_order[branch] = total_order

    best_selled_branches = dict(sorted(branches_total_order.items(), key=lambda x: x[1], reverse=True))

    return render(request, "home.html", {"data": best_sold_foods, "best_selled_branches": best_selled_branches})


class FoodAdminViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAdminUser]


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodRestaurantCategory.objects.all()
    serializer_class = FoodCategorySerializer
    permission_classes = [permissions.IsAdminUser]


class MealViewSet(viewsets.ModelViewSet):
    queryset = MealCategory.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAdminUser]


class MealCategoryViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodRestaurantCategory
    permission_classes = [permissions.IsAdminUser]


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


class AdminPanel(SuperUserRequiredMixin, TemplateView):
    template_name = "restaurant/admin_panel/admin_panel.html"


def orders_list(request):
    data = Order.objects.all().order_by("-id")
    return render(request, "restaurant/orders_list.html", {"data": data})


# def update_item(request):
#     data = json.loads(request.body)
#     foodId = data["foodId"]
#     action = data["action"]
#
#     print("foodId: ", foodId)
#     print("Action: ", action)
#
#     customer = request.user
#     food = Food.objects.get(id=foodId)
#     order = Order.objects.get_or_create(user=customer)
#
#     # menu_order, created = MenuOrder.objects.get_or_create(order=order, food=food)
#
#     # if action == "add":
#     #     menu_order.number = (menu_order.number + 1)
#     # elif action == "remove":
#     #     menu_order.number = (menu_order.number - 1)
#     #
#     # menu_order.save()
#
#     # if menu_order.number <= 0:
#     #     menu_order.delete()
#
#     return JsonResponse("It was added", safe=False)
