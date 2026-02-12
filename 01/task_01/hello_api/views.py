from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

# Create your views here.

@api_view(["GET"])
def hello_api(request):

    greetings = {
        "pl": "Cześć!",
        "en": "Hello!",
        "de": "Hallo!",
        "it": "Ciao!",
        "default": "Hej!"
    }

    lang = request.query_params.get("lang", "default")

    return Response({
        "message": greetings[lang]
    })