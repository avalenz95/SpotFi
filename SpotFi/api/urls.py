from django.urls import path
from api.views import PlaylistList

urlpatterns = [
    path('playlists/', PlaylistList.as_view(), name='playlist_list'),
]