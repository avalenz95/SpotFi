from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from playlists.models import Song, Playlist
from os import getenv
from dotenv import load_dotenv

load_dotenv()
client = getenv("CLIENT_ID")
secret = getenv("CLIENT_SECRET")

class IndexView(ListView):
    def get(self, request):
        return render(request, 'index.html')


class PlaylistListView(ListView):

    def get(self, request):
        return render(request, 'playlists/plist.html')

