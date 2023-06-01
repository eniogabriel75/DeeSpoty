from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True, unique=True)
    name = models.CharField(max_length=100)

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    total_tracks = models.CharField(max_length=50, null=True)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    informations = models.CharField(max_length=200, default="info")
    tracks = models.CharField(max_length=50, default="music")

class Album(models.Model):
    release_year = models.CharField(max_length=20, default="Valor padrão")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Track(models.Model):
    id = models.CharField(max_length=255, primary_key=True, unique=True)
    playlists = models.ManyToManyField(Playlist)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, )
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    genre = models.CharField(max_length=10, null=True )
    lyrics = models.CharField(max_length=255, null=True)

class Creator(models.Model):
    creator_id = models.CharField(max_length=255) #primary_key=True, unique=True)  
    name = models.CharField(max_length=20)

class PodCasts(models.Model):
    id = models.CharField(max_length=255, primary_key=True, unique=True)  
    title = models.CharField(max_length=20)  
    description = models.CharField(max_length=150)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

class CollectionTracks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE)
    total_tracks = models.CharField(max_length=255)