from django.urls import path
from . import views

urlpatterns = [
    path('playlists/', views.PlaylistListView.as_view(), name='playlist-list-view'),
]