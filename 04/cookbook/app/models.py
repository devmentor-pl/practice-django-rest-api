from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name


# Create your models here.
