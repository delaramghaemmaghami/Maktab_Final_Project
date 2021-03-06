import json

import accounts.mixins
from django.contrib import messages
from django.db.models import Q, Sum
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from rest_framework import viewsets, permissions

from .serializer import *
from .forms import *
from accounts.models import Customer


def home(request):
    foods = Food.objects.filter(
        Q(food_rel__menu_rel__order__status="ثبت") |
        Q(food_rel__menu_rel__order__status='ارسال') |
        Q(food_rel__menu_rel__order__status='تحویل')).annotate(total_order=Sum("food_rel__menu_rel__number")).order_by(
        "-total_order")

    branches = Branch.objects.filter(
        Q(branch_rell__status="ثبت") |
        Q(branch_rell__status='ارسال') |
        Q(branch_rell__status='تحویل')).annotate(total_order=Sum("branch_rell__order_rel__number")).order_by(
        "-total_order")

    return render(request, "home.html", {"data": foods, "best_selled_branches": branches})


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


class AdminPanel(accounts.mixins.SuperUserRequiredMixin, TemplateView):
    template_name = "restaurant/admin_panel/admin_panel.html"


def orders_list(request):
    data = Order.objects.all().order_by("-id")
    return render(request, "restaurant/orders_list.html", {"data": data})


def update_item(request):
    global customer
    data = json.loads(request.body)

    menuId = data["menuId"]
    action = data["action"]

    menu = Menu.objects.get(id=menuId)
    branchId = menu.branch.id
    branch = Branch.objects.get(id=branchId)

    if request.user.is_authenticated:
        customer = request.user

    if not request.user.is_authenticated:
        device = request.COOKIES["device"]
        customer, created = Customer.objects.get_or_create(device=device)

        order, order_create = Order.objects.get_or_create(user=customer, branch=branch)

        menu_order, menu_order_create = MenuOrder.objects.get_or_create(order=order, menu=menu)

    menu_orders = MenuOrder.objects.filter(order__user__device=str(request.COOKIES["device"])).order_by("-id")

    if menu_orders:
        mo = menu_orders[0].order.branch.name
        if MenuOrder.objects.filter(Q(order__user__device=str(request.COOKIES["device"])) & ~Q(order__branch__name=mo)):
            messages.add_message(request, messages.INFO, "You can't order from different branches!")
            x = MenuOrder.objects.filter(Q(order__user__device=str(request.COOKIES["device"])) & ~Q(order__branch__name=mo)).delete()

    if action == "add":
        menu_order.number = (menu_order.number + 1)
        menu_order.price += int(menu.price)

    menu_order.save()

    if menu_order.number <= 0:
        menu_order.delete()

    return JsonResponse("It was added", safe=False)


def cart(request):
    data = MenuOrder.objects.filter(order__user__device=str(request.COOKIES["device"])).order_by("-id")

    result = 0

    if data:
        for d in data:
            result += d.price

        order = Order.objects.get(id=data[0].order.id)
        order.total_price = result
        order.save()

    return render(request, "restaurant/user_cart.html", {"data": data, "result": result})


def delete_food_order(request, id):
    menu_order = MenuOrder.objects.get(id=id).delete()
    return HttpResponseRedirect("/cart")


def update_cart(request):
    data = json.loads(request.body)
    foodId = data["foodId"]
    number = data["number"]
    # customer = request.user
    menu_order = MenuOrder.objects.get(id=foodId)
    menuId = menu_order.menu.id
    menu = Menu.objects.get(id=menuId)

    if int(number) <= menu.inventory:
        menu_order.number = int(number)
        menu_order.price = menu.price * int(number)
        menu_order.save()

    return JsonResponse("It was added", safe=False)
