from django.db import models



class Playlists(model.Models):
    title = models.CharField(max_length=30)
    number_of_songs = model.PositiveIntegerField()


class Song(model.Models):
    title = models.CharField(max_length=30)
    runtime = models.DecimalField(decimal_places=2)
    artist = models.CharField(max_length=30)
    playlists = models.ForeignKey(Playlists, on_delete=models.CASCADE)


