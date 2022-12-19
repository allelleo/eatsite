from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from slugify import slugify
from .apps import HomeConfig
from .models import Recipe, Category
from eatsite.settings import MEDIA_URL
import random


# Create your views here.
class Home(View):
    template_name = 'home/index.html'

    def context(self):
        MostPopularRecipes = Recipe.objects.order_by('-views')[0:10]
        AllCategories = [[cat.title, slugify(cat.title)] for cat in Category.objects.all()]
        RandomRecipeTwo = random.sample(list(Recipe.objects.all()), 2)
        LastSixRecipes = Recipe.objects.order_by('-id')[0:8]
        return {
            'SiteName': HomeConfig.SiteName,
            'SiteLink': HomeConfig.SiteLink,
            "Dzen": HomeConfig.DzenLink,
            "Vk": HomeConfig.VkLink,
            "Tg": HomeConfig.TelegramLink,

            "SalatRecipeCounter": Category.objects.get(slug="salaty").views,
            "FishRecipeCounter": Category.objects.get(slug="ryba").views,
            "ChickenRecipeCounter": Category.objects.get(slug="kuritsa").views,
            "MeatRecipeCounter": Category.objects.get(slug="miaso").views,
            "ProperNutritionRecipeCounter": Category.objects.get(slug="dieta").views,
            "CoffeeRecipeCounter": Category.objects.get(slug="kofe").views,
            "TeaRecipeCounter": Category.objects.get(slug="chai").views,
            "SoupRecipeCounter": Category.objects.get(slug="supy").views,
            "SnackRecipeCounter": Category.objects.get(slug="perekus").views,
            "SweetRecipeCounter": Category.objects.get(slug="sladosti").views,
            "DrinkRecipeCounter": Category.objects.get(slug="napitki").views,

            "MostPopularRecipes": MostPopularRecipes,
            "AllCategories": AllCategories,
            "RandomRecipeTwo": RandomRecipeTwo,
            "LastSixRecipes": LastSixRecipes,
            "media": MEDIA_URL,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context())


class GetRecipe(View):
    template_name = 'home/recipe.html'

    def context(self, slug):
        recipe = Recipe.objects.get(slug=slug)
        if recipe:
            MostPopularRecipes = Recipe.objects.order_by('-views')[0:15]
            AllCategories = [[cat.title, slugify(cat.title)] for cat in Category.objects.all()]
            recipe.views = recipe.views + 1
            recipe.category.views += 1
            recipe.save()
            recipe.category.save()
            return {
                "Recipe": recipe,
                'Ingredients': recipe.ingredients.split('\n\n'),
                "Steps": [[i + 1, recipe.steps.split('\n\n')[i]] for i in range(len(recipe.steps.split('\n\n')))],
                'SiteName': HomeConfig.SiteName,
                'SiteLink': HomeConfig.SiteLink,
                "MostPopularRecipes": MostPopularRecipes,
                "AllCategories": AllCategories,
                "media": MEDIA_URL,
                "Dzen": HomeConfig.DzenLink,
                "Vk": HomeConfig.VkLink,
                "Tg": HomeConfig.TelegramLink,
            }
        else:
            return 500

    def get(self, request, slug, *args, **kwargs):
        data = self.context(slug)
        if data != 500:
            return render(request, self.template_name, data)
        else:
            return HttpResponse("Error 500")
