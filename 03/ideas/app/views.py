from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

ideas = []
next_id = 1


class IdeaAPIView(APIView):

    def get(self, request):
        return Response(ideas, status=200)

    def post(self, request):
        global next_id
        idea = request.data.get('description')
        if idea:
            new_idea = {'id': next_id, 'description': idea}
            ideas.append(new_idea)
            next_id += 1
            return Response(new_idea, status=201)
        return Response({'error': 'Brakuje pola description'}, status=400)

# Create your views here.
