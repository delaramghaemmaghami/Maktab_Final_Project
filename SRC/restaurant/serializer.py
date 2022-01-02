from rest_framework import serializers
from .models import *


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRestaurantCategory
        fields = "__all__"


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = "__all__"
