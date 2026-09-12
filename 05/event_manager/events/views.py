from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import action
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=['get'], url_path='recent')
    def recent(self, request):
        today = timezone.now().date()
        end_date = today + timedelta(days=7)

        queryset = self.get_queryset()
        queryset = queryset.filter(date__gte=today, date__lte=end_date)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
