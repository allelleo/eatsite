from django.db import models
from slugify import slugify


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    views = models.IntegerField(default=0)


class CookingLevel(models.Model):
    title = models.CharField(max_length=100)


class KitchenType(models.Model):
    title = models.CharField(max_length=100)


class Recipe(models.Model):
    title = models.CharField(max_length=150)  # Название рецепта
    quote = models.CharField(max_length=300)  # Краткое описание
    slug = models.CharField(max_length=200, null=True, blank=True)  # Ссылка на рецепт
    published_date = models.DateTimeField(auto_now_add=True)  # Дата публикации

    steps = models.TextField()  # Шаги готовки
    ingredients = models.TextField()  # Ингредиенты

    preview = models.ImageField(upload_to='preview/')  # Фото блюда
    views = models.IntegerField(default=0)  # Количество просмотров
    tags = models.CharField(max_length=200)  # Теги

    author_name = models.CharField(max_length=150)  # Имя автора
    author_link = models.CharField(max_length=200)  # Ссылка на автора

    CookingTime = models.IntegerField(default=0)  # Время готовки
    PortionCounter = models.IntegerField(default=1)  # Количество порций

    CaloricContent = models.IntegerField(default=0)  # Калорийность
    Squirrels = models.IntegerField(default=0)  # Белки
    Fats = models.IntegerField(default=0)  # Жиры
    Carbohydrates = models.IntegerField(default=0)  # Углеводы
    Water = models.IntegerField(default=0)  # Вода
    DietaryFiber = models.IntegerField(default=0)  # Пищевые волокна

    CookingLevel = models.ForeignKey(CookingLevel, on_delete=models.PROTECT)  # Сложность готовки
    KitchenType = models.ForeignKey(KitchenType, on_delete=models.PROTECT)  # Тип кухни
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # категория

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + str(self.pk)
        super().save(*args, **kwargs)
