from django.core.validators import MinValueValidator
from django.db import models


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
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    meal_category = models.ManyToManyField(MealCategory, related_name="meal")
    food_restaurant_category = models.ForeignKey(FoodRestaurantCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    inventory = models.PositiveIntegerField()
    price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3)

    food = models.ManyToManyField(Food, related_name="food")
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
    total_price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.branch}"


class FoodOrder(models.Model):
    pass
