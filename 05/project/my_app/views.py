from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import action


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=["get"], url_path="recent")
    def recent(self, request):
        today = timezone.localdate()
        seven_days = today + timedelta(days=7)

        events = Event.objects.filter(date__gte=today, date__lte=seven_days)
        serializer = EventSerializer(events, many=True)

        return Response(serializer.data)
