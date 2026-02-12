from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import date, timedelta
from .models import Event

# Create your views here.


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=["get"], url_path="recent")
    def recent(self, request):
        today = date.today()
        next_week = today + timedelta(days=7)

        events = Event.objects.filter(
            date__gte=today,
            date__lte=next_week
        ).order_by("date")

        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
