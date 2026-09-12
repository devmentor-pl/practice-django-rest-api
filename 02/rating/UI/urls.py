from django.urls import path
from .views import rate_movie_view

urlpatterns = [
    path('api/rate/', rate_movie_view, name='rate-movie'),]
