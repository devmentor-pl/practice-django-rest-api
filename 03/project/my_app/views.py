from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

ideas = []
next_id = 1


class IdeaAPIView(APIView):
    def get(self, request):
        return Response(ideas)

    def post(self, request):
        global next_id

        description = request.data.get("description")

        if not isinstance(description, str) or not description.strip():
            return Response(
                {"error": "Opis jest wymagany"},
                status=status.HTTP_400_BAD_REQUEST
            )

        new_idea = {"id": next_id, "description": description}
        ideas.append(new_idea)
        next_id += 1
        return Response(new_idea, status=status.HTTP_201_CREATED)
