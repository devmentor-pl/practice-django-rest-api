from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def rate_movie_view(request):
    movie = request.data.get('movie')
    rating = request.data.get('rating')
    
    if not isinstance(movie, str) or not movie.strip():
        return Response(
            {"error": "Nazwa filmu jest wymagana"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(rating, int) and not isinstance(rating, bool) and 1 <= rating <= 10:
        return Response(
            {"message": f"Oceniono film '{movie}' na {rating}/10"}, 
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {"error": "Ocena musi być liczbą od 1 do 10"}, 
        status=status.HTTP_400_BAD_REQUEST
    )

    
