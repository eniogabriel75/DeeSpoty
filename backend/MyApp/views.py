from rest_framework import generics
from MyApp.models import User, Playlist, Track, Artist
from MyApp.serializers import UserSerializer, PlaylistSerializer, TrackSerializer, ArtistSerializer

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
