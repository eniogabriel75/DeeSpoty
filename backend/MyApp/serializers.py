from rest_framework import serializers
from MyApp.models import User, Playlist, Track,Artist, Album, Creator, PodCasts, CollectionTracks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["name","total_tracks"]
    def duration(self,instance):
        
        return instance.duration



class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'
class PodCastsSerialzier(serializers.ModelSerializer):
    class Meta:
        moedl = PodCasts
        fields = '__all__'

class CollectionTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionTracks
        fields = '__all__'