from django.urls import path
from .views import IdeaAPIView

urlpatterns = [
    path('api/ideas/', IdeaAPIView.as_view(), name='user-ideas'),]
