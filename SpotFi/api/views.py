from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from playlists.models import Playlist
from api.serializers import PlaylistSerializer

class PlaylistList(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()[:20]
        data = PlaylistSerializer(playlists, many=True).data
        return Response(data)
