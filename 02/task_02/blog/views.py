from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(["POST"])
def rate_movie_view(request):

    rating = request.data.get("rating")
    movie = request.data.get("movie")

    if rating is None:

        return Response(
            {"error": "Brak oceny"},
            status=400
        )

    try:
        rating = int(rating)

    except (TypeError, ValueError):
        return Response(
            {"error": "Wpisana ocena nie jest liczba"},
            status=400
        )

    if rating < 1 or rating > 10:
        return Response(
            {"error": "Ocena nie jest w skali 1-10"},
            status=400
        )

    if not movie:
        return Response(
            {"error": "Brak filmu"},
            status=400
        )

    return Response(
        {"message": f"Oceniono {movie} na {rating}/10"},
        status=201
    )
