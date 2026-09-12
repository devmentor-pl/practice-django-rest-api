from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def rate_movie_view(request):
    movie = request.data.get('movie')
    rating = request.data.get('rating')
    try:
        rating = int(rating)
    except (ValueError, TypeError):
        return Response({
            'error': 'Ocena musi być liczbą.'
        }, status=400)
    if 1 <= rating <= 10:
        return Response({
            'message': f'Oceniono film "{movie}" na {rating}/10.'
        }, status=201)

    return Response({
        'error': 'Ocena musi być liczbą od 1 do 10.'
    }, status=400)

# Create your views here.
