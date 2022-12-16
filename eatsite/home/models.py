from django.db import models
from slugify import slugify


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    views = models.IntegerField(default=0)


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    quote = models.CharField(max_length=300)
    slug = models.CharField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    steps = models.TextField()
    preview = models.ImageField(upload_to='preview/')
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author_name = models.CharField(max_length=150)
    author_link = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + str(self.pk)
        super().save(*args, **kwargs)
