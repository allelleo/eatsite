from django.db import models
from slugify import slugify
import os


def path_and_rename(instance, filename):
    slug = slugify(instance.title)
    upload_to = 'preview_photo/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}_{}.{}'.format(slug, instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(slug, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class CookingLevel(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class KitchenType(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=400)  # Название рецепта
    quote = models.CharField(max_length=1500)  # Краткое описание
    slug = models.CharField(max_length=450, null=True, blank=True)  # Ссылка на рецепт
    published_date = models.DateTimeField(auto_now_add=True)  # Дата публикации

    steps = models.TextField()  # Шаги готовки
    ingredients = models.TextField()  # Ингредиенты

    preview = models.ImageField(upload_to=path_and_rename)  # Фото блюда
    views = models.IntegerField(default=0)  # Количество просмотров
    tags = models.CharField(max_length=200)  # Теги

    author_name = models.CharField(max_length=150)  # Имя автора
    author_link = models.CharField(max_length=200)  # Ссылка на автора

    CookingTime = models.IntegerField(default=0)  # Время готовки
    PortionCounter = models.IntegerField(default=1)  # Количество порций

    CaloricContent = models.CharField(max_length=400)  # Калорийность
    Squirrels = models.CharField(max_length=400)  # Белки
    Fats = models.CharField(max_length=400)  # Жиры
    Carbohydrates = models.CharField(max_length=400)  # Углеводы
    Water = models.CharField(max_length=400)  # Вода

    CookingLevel = models.ForeignKey(CookingLevel, on_delete=models.PROTECT)  # Сложность готовки
    KitchenType = models.ForeignKey(KitchenType, on_delete=models.PROTECT)  # Тип кухни
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # категория

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + str(self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


'''from .load_data import LoadCategories, LoadKitchenTypes

LoadKitchenTypes(KitchenType)
LoadCategories(Category)'''
