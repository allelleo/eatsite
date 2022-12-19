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
        MostPopularRecipes = Recipe.objects.order_by('-views')[0:6]
        AllCategories = [[cat.title, slugify(cat.title)] for cat in Category.objects.all()]
        RandomRecipeTwo = random.sample(list(Recipe.objects.all()), 2)
        LastSixRecipes = Recipe.objects.order_by('-id')[0:6]
        return {
            'SiteName': HomeConfig.SiteName,
            'SiteLink': HomeConfig.SiteLink,
            "Dzen": HomeConfig.DzenLink,
            "Vk": HomeConfig.VkLink,
            "Tg": HomeConfig.TelegramLink,
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

    def GetRecipeBySlug(self, slug):
        RecipeObject = Recipe.objects.get(slug=slug)
        RecipeObject.views += 1
        RecipeObject.category.views += 1
        RecipeObject.save()
        RecipeObject.category.save()
        return RecipeObject

    def context(self, slug):
        MostPopularRecipes = Recipe.objects.order_by('-views')[0:6]
        AllCategories = [[cat.title, slugify(cat.title)] for cat in Category.objects.all()]
        recipe = self.GetRecipeBySlug(slug)
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

    def get(self, request, slug, *args, **kwargs):
        return render(request, self.template_name, self.context(slug))
