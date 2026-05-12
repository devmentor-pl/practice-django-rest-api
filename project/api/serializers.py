from rest_framework import serializers

from .models import Recipe, Ingredient, Event


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        extra_kwargs = {'name': {'validators': []}}  # Disable unique validation for name field


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients']
        
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_data['name'])
            recipe.ingredients.add(ingredient)
        return recipe
    
    
######### ex. 5 ###################

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'