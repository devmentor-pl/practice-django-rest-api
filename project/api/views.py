from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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


@api_view(['POST'])
def rate_movie_view(request):
    movie = request.data.get('movie')
    rating = request.data.get('rating')
    if not movie or rating is None:
        return Response({'error': 'Film i ocena są wymagane.'}, status=400)
    if 0 <= rating <= 10:
        return Response({'message': f'Oceniono film "{movie}" na {rating}/10.'})
    return Response({'error': 'Ocena musi być liczbą od 1 do 10.'}, status=400)
    
        