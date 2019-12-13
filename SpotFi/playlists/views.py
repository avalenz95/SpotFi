from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from playlists.models import Song, Playlist
from django.urls import reverse_lazy
from .forms import PlaylistForm
from os import getenv
from dotenv import load_dotenv
import requests

# load_dotenv()
# client = getenv("CLIENT_ID")
# secret = getenv("CLIENT_SECRET")
# /
# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Authorization': f'Basic {client}:{secret}',
# }

# params = (
#     ('q', 'woop woop'),
#     ('type', 'track'),
#     ('limit', '25'),
# )

# response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

# GET https://accounts.spotify.com/authorize?client_id=f7f39a20f2734d20b341b4f02d93e335&redirect
# =
# Set it to “token”.
# redirect_uri	Required.
# The URI to redirect to after the user grants/denies permission. This URI needs to be entered in the URI whitelist that you specify when you register your application.
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.get('https://api.spotify.com/v1/search?q=woop%20woop&type=track&limit=25', headers=headers)

class IndexView(ListView):
    def get(self, request):
        return render(request, 'index.html')


class PlaylistListView(ListView):

    def get(self, request):
        return render(request, 'playlists/plist.html')
        
class PlaylistCreateView(CreateView):

      #user wants to submit form
  def get(self, request, *args, **kwargs):
      #get form
      context = {'form': PlaylistForm()}
      #pass form to wiki/newpage and render template
      return render(request, 'playlists/newplaylist.html', context)

  #user has submitted form
  def post(self, request, *args, **kwargs):
      #form submitted via post request
      form = PlaylistForm(request.POST)
      #form validation check
      if form.is_valid():
          #save form
          playlist = form.save()
          #redirect the user to home 
          return HttpResponseRedirect(reverse_lazy('index'))

      #render the form again if it is not valid
      return render(request, 'playlists/newplaylist.html', {'form': form})
