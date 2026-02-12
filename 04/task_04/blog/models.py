from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Ingredient(models.Model):

    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
