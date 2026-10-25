from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello_view(request):
    lang = request.query_params.get("lang")

    lang_map = {
        "pl": "Cześć!",
        "en": "Hello!",
        "de": "Hallo!",
    }

    message = lang_map.get(lang, "Hej!")
    return Response({"message": message})
