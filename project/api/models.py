from django.db import models



class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    
    def __str__(self):
        return self.title