from django.shortcuts import render
from django.views import View

from .apps import HomeConfig


# Create your views here.
class Home(View):
    template_name = 'home/index.html'

    def context(self):
        return {
            'SiteName': HomeConfig.SiteName,
            "SalatRecipeCounter": 666,
            "FishRecipeCounter": 666,
            "ChickenRecipeCounter": 666,
            "MeatRecipeCounter": 666,
            "ProperNutritionRecipeCounter": 666,
            "CoffeeRecipeCounter": 666,
            "TeaRecipeCounter": 666,
            "SoupRecipeCounter": 666,
            "SnackRecipeCounter": 666,
            "SweetRecipeCounter": 666,
            "DrinkRecipeCounter": 666,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context())
