from django import forms
from .models import Playlist 


class PlaylistForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Playlist
        fields = ['title', 'author', 'description']