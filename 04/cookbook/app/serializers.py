from rest_framework import serializers
from .models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients']

    def create(self, validated_data):
        ingredients_names = validated_data.pop('ingredients', [])

        recipe = Recipe.objects.create(**validated_data)

        for name in ingredients_names:
            Ingredient.objects.create(name=name, recipe=recipe)

        return recipe

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ingredients'] = [
            ingredient.name for ingredient in instance.ingredients.all()]
        return representation
