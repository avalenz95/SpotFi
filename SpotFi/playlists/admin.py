from django.contrib import admin
from playlists.models import Song, Playlist

# Register your models here.

admin.site.register(Song)
admin.site.register(Playlist)