from django.contrib import admin
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "food_restaurant_category", "meal_categories"]
    list_display_links = ["name"]

    fieldsets = [("CATEGORIES", {'fields': ("food_restaurant_category", "meal_category")}),
                 ("OTHERS", {'fields': ("name", "image")})]


class RestaurantBranches(admin.TabularInline):
    model = Branch


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]

    inlines = [RestaurantBranches]


class BranchAddressRestaurant(admin.TabularInline):
    model = Branch


class BranchAddressAdmin(admin.ModelAdmin):
    list_display = ["id", "city", "address"]
    list_display_links = ["address"]

    inlines = [BranchAddressRestaurant]


class MealCategoryFood(admin.TabularInline):
    model = Food.meal_category.through


class MealCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]

    inlines = [MealCategoryFood]


class FoodRestaurantCategoryFood(admin.TabularInline):
    model = Food


class FoodRestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]

    inlines = [FoodRestaurantCategoryFood]


class BranchAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_main", "food_restaurant_category", "restaurant"]
    list_display_links = ["name"]


class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "food", "inventory"]
    list_display_links = ["food"]


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(BranchAddress, BranchAddressAdmin)
admin.site.register(MealCategory, MealCategoryAdmin)
admin.site.register(FoodRestaurantCategory, FoodRestaurantCategoryAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Menu, MenuAdmin)
