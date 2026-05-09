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
    
        
ideas = []
next_id = 1

class IdeaAPIView(APIView):
    def get(self, request):
        return Response(ideas)
    
    def post(self, request):
        global next_id
        description = request.data.get('description')
        if not description:
            return Response({'error': 'Opis jest wymagany.'}, status=400)
        
        new_idea = {'id': next_id, 'description': description}
        ideas.append(new_idea)
        next_id += 1
        return Response(ideas, status=201)
    
