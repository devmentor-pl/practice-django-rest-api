from django.urls import path
from .views import RecipeAPIView

urlpatterns = [
    path("api/recipes/", RecipeAPIView.as_view(), name="api_recipes")
]
