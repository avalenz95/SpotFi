from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from playlists.models import Song, Playlist


class PlaylistListView(ListView):

    def get(self, request):
        """ GET a list of Pages. """
        #pages = Page.objects.order_by('-created')
        #pages = Page.objects.order_by('created'.desc())
        pages = self.get_queryset().all().order_by('-created')
        #pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

