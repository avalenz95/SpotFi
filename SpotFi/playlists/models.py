
from django.conf import settings
from django.db import models

class Playlist(models.Model):
    title = models.CharField(max_length=30)
    number_of_songs = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=30)
    runtime = models.DecimalField(max_digits=3, decimal_places=2)
    artist = models.CharField(max_length=30)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


