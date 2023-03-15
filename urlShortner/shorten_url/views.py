from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from shorten_url.models import ShortUrlModel
from shorten_url.serializers import ShortUrlSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ShortenUrl(APIView):
    """Shorten a URL."""
    permission_classes = [IsAuthenticated] # User must logged in to create short URL
    
    def post(self, request):
        data = {
            'url': request.data.get('url'),
            'short_id': ShortUrlModel.generate_short_id(),
        }

        serializer = ShortUrlSerializer(data=data)

        # if raised exception, it automatically
        # returns a 400 response with errors
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, 201)


class GetOriginalUrl(APIView):
    """Decode a URL short id into a the Original URL."""

    def get(self, request, short_id: str):
        try:
            obj = ShortUrlModel.objects.get(short_id=short_id)
            obj.increase_short_id_counter()
        except ObjectDoesNotExist:
            return Response({'error': 'Short url id does not exist.'}, 400)

        serializer = ShortUrlSerializer(obj)
        return redirect(obj.url)