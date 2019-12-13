from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from playlists.models import Song, Playlist


class PlaylistListView(ListView):

    def get(self, request):
        return render(request, 'plist.html')

