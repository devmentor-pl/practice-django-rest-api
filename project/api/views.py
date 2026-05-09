from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_view(request):
    lang = request.GET.get('lang', 'en')
    if lang =='pl':
        return Response({'message': 'Witaj!'})
    if lang == 'es':
        return Response({'message': '¡Hola!'})
    if lang == 'fr':
        return Response({'message': 'Bonjour!'})
    if lang == 'de':
        return Response({'message': 'Hallo!'})
    return Response({'message': 'Hello!'})