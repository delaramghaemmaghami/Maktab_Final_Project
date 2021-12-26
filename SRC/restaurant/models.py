from django.core.validators import MinValueValidator
from django.db import models
from accounts.models import Staff, Customer


class Restaurant(models.Model):
    name = models.CharField(max_length=100)


class BranchAddress(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class MealCategory(models.Model):
    name = models.CharField(max_length=100)


class FoodRestaurantCategory(models.Model):
    name = models.CharField(max_length=100)


class Branch(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_main = models.BooleanField()
    description = models.TextField(max_length=500)

    food_restaurant_category = models.OneToOneField(FoodRestaurantCategory, on_delete=models.CASCADE)  # todo: FK
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    branch_address = models.OneToOneField(BranchAddress, on_delete=models.CASCADE)
    manager = models.OneToOneField(Staff, on_delete=models.CASCADE)


class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    meal_category = models.ManyToManyField(MealCategory, related_name="meal")
    food_restaurant_category = models.ForeignKey(FoodRestaurantCategory, on_delete=models.CASCADE)


class Menu(models.Model):
    inventory = models.PositiveIntegerField()
    price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3)

    food = models.ManyToManyField(Food, related_name="food")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class Order(models.Model):
    status_choices = [
        ("not paid", "not paid"),
        ("submitted", "submitted"),
        ("sent", "sent"),
        ("delivered", "delivered")
    ]
    status = models.CharField(max_length=10, choices=status_choices, default="not paid")
    total_price = models.DecimalField(validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class FoodOrder(models.Model):
    pass
