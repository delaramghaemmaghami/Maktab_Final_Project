from django.db import transaction
from django.forms import ModelForm
from .models import *


class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'image', 'meal_category', "food_restaurant_category", 'description']

    @transaction.atomic
    def save(self):
        obj = super().save(commit=False)
        obj.name = self.cleaned_data.get("name")
        obj.image = self.cleaned_data.get("image")
        obj.meal_category = self.cleaned_data.get("meal_category")
        obj.food_restaurant_category = self.cleaned_data.get("food_restaurant_category")
        obj.description = self.cleaned_data.get("description")
        obj.save()
        return obj

    def __init__(self, *args, **kwargs):
        super(AddFoodForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['meal_category'].widget.attrs['class'] = 'form-control'
        self.fields['food_restaurant_category'].widget.attrs['class'] = 'form-control'


class AddMealCategoryForm(ModelForm):
    class Meta:
        model = MealCategory
        fields = ['name']

    @transaction.atomic
    def save(self):
        obj = super().save(commit=False)
        obj.save()
        return obj

    def __init__(self, *args, **kwargs):
        super(AddMealCategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'


class AddFoodRestaurantCategoryForm(ModelForm):
    class Meta:
        model = FoodRestaurantCategory
        fields = ['name']

    @transaction.atomic
    def save(self):
        obj = super().save(commit=False)
        obj.save()
        return obj

    def __init__(self, *args, **kwargs):
        super(AddFoodRestaurantCategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
