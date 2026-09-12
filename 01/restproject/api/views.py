from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_view(request):
    lang = request.query_params.get('lang')
    messages = {
        "pl": "Cześć!",
        "en": "Hello!",
        "de": "Hallo!"
    }
    message = messages.get(lang, "Hej!")
    return Response({
        'message': message})

    # Create your views here.
