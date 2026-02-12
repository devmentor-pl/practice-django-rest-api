from .models import Recipe, Ingredient
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ["id", "title", "ingredients"]

    def create(self, data):
        ingredients_data = data.pop("ingredients")
        recipe = Recipe.objects.create(**data)

        for ingredient in ingredients_data:
            Ingredient.objects.create(
                recipe=recipe,
                **ingredient
            )
        return recipe


class RecipeAPIView(APIView):

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Poprawnie dodano przepis"}, status=201)

        return Response(serializer.errors, status=400)
