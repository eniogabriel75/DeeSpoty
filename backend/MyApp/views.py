from rest_framework import generics
from MyApp.models import User, Playlist, Track,Artist, Album, Creator, PodCasts, CollectionTracks, CollectionPods
from MyApp.serializers import UserSerializer, PlaylistSerializer, TrackSerializer, ArtistSerializer, AlbumSerializer, CreatorSerializer, PodCastsSerialzier, CollectionTracksSerializer, CollectionPodsSerializer

class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaylistViewSet(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class TrackViewSet(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
class ArtistViewSet(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class CreatorViewSet(generics.ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

class PodCastsViewSet(generics.ListAPIView):
    queryset = PodCasts.objects.all()
    serializer_class = PodCastsSerialzier
    
class CollectionTracksViewSet(generics.ListAPIView):
    queryset = CollectionTracks.objects.all()
    serializer_class = CollectionTracksSerializer

class CollectionPodsViewSet (generics.ListAPIView):
    queryset = CollectionPods.objects.all()
    serializer_class = CollectionPodsSerializer