from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('playlists/', views.PlaylistListView.as_view(), name='playlist-list-view'),
    path('playlists/create-playlist', views.PlaylistCreateView.as_view(), name='playlist-create' )
]