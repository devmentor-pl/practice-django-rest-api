from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


ideas = [{"id": 1, "description": "Zbudować aplikację do zarządzania budżetem"}]
next_id = 2


class IdeaAPIVIEV(APIView):

    def get(self, request):
        return Response(ideas)

    def post(self, request):
        global next_id

        idea_description = request.data.get("description")
        if not idea_description:
            return Response("Brak opisu pomyslu", status=400)

        new_idea = {"id": next_id, "description": idea_description}
        ideas.append(new_idea)
        next_id += 1

        return Response("Dodano nowy pomysl do listy", status=201)
