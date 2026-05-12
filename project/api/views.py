import datetime
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RecipeSerializer, EventSerializer
from .models import Recipe, Event



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
    

class IdeaDetailAPIView(APIView):
    def get_idea(self, idea_id):
        return next((idea for idea in ideas if idea_id == idea['id']), None)
    
    def get(self, request, idea_id):
        idea = self.get_idea(idea_id)
        if not idea:
            return Response({"error": "Not found"}, status=404)
        return Response(idea)
    
    def put(self, request, idea_id):
        idea = self.get_idea(idea_id)
        if not idea:
            return Response({"error": "Not found"}, status=404)
        idea['description'] = request.data.get('description', idea['description'])
        return Response(idea)
    
    def delete(self, request, idea_id):
        idea = self.get_idea(idea_id)
        if not idea:
            return Response({"error": "Not found"}, status=404)
        ideas.remove(idea)
        return Response(status=204)
        
    
class RecipeAPIView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=200)
        
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

########### ex. 5 #########################
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer
    
    @action(methods=['get'], detail=False)
    def recent(self, request):
        today = datetime.date.today()
        future_date = today + datetime.timedelta(days=7)
        recent_events = Event.objects.filter(date__gte=today, date__lte=future_date).order_by('date')[:5]
        serializer = self.get_serializer(recent_events, many=True)
        return Response(serializer.data)