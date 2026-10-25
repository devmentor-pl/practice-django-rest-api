from rest_framework import serializers
from .models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class RecipeSerializer(serializers.ModelSerializer):

    ingredients = serializers.ListField(
        child=serializers.CharField(max_length=100), write_only=True)

    class Meta:
        model = Recipe
        fields = ["id", "title", "ingredients"]

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients", [])
        recipe = Recipe.objects.create(**validated_data)
        for element in ingredients_data:
            Ingredient.objects.create(recipe=recipe, name=element)
        return recipe

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["ingredients"] = IngredientSerializer(
            instance.ingredients.all(), many=True).data
        return data
