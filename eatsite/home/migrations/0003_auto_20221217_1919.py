# Generated by Django 3.0 on 2022-12-17 16:19

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221217_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preview',
            field=models.ImageField(upload_to=home.models.path_and_rename),
        ),
    ]