import os.path

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BranchAddress(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city} | {self.address}"


class MealCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodRestaurantCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_main = models.BooleanField()
    description = models.TextField(max_length=500)

    food_restaurant_category = models.OneToOneField(FoodRestaurantCategory, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    branch_address = models.OneToOneField(BranchAddress, on_delete=models.CASCADE)
    manager = models.OneToOneField("accounts.Staff", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Food(models.Model):
    def upload_path(self, file_name: str):
        extention = file_name.split(".")[-1]
        file_name = f"{self.name}.{extention}"
        path = "food"
        return os.path.join(path, file_name)

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    meal_category = models.ManyToManyField(MealCategory, related_name="meal")
    food_restaurant_category = models.ManyToManyField(FoodRestaurantCategory, related_name="food_cat")

    def meal_categories(self):
        return "\n ,".join([meal.name for meal in self.meal_category.all()])

    def food_restaurant_categories(self):
        return "\n ,".join([food_cat.name for food_cat in self.food_restaurant_category.all()])

    def image_tag(self):
        return mark_safe("<img src='%s' width='50' width='50'/>" % (self.image.url))

    def __str__(self):
        return self.name


class Menu(models.Model):
    inventory = models.PositiveIntegerField()
    price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3)

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food} | {self.branch}"


class Order(models.Model):
    status_choices = [
        ("سفارش", "سفارش"),
        ("ثبت", "ثبت"),
        ("ارسال", "ارسال"),
        ("تحویل", "تحویل")
    ]
    status = models.CharField(max_length=10, choices=status_choices, default="not paid")
    total_price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3, default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user_address = models.OneToOneField("accounts.UserAddress", on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return f"{self.user} | {self.branch}"


class MenuOrder(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3, default=0.0)

    def __str__(self):
        return f"{self.menu} | {self.order}"
