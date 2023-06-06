from rest_framework import serializers
from MyApp.models import User, Playlist, Track,Artist, Album, Creator, PodCasts, CollectionTracks, CollectionPods

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]

class PlaylistSerializer(serializers.ModelSerializer):
    #duration_playlist = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ["name", "total_tracks"]

    """def duration_playlist(self, instance):
        total_duration = 0
        for track in instance.tracks.all():
            total_duration += track.duration
        return total_duration"""


class TrackSerializer(serializers.ModelSerializer):
    duration_track = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ["id", "playlist","title", "artist", "album", "genre", "lyrics","duration_track"]

    def duration_track(self, instance):
        # Cálculo da duração da faixa em formato HH:MM:SS
        duration_seconds = instance.duration
        minutes, seconds = divmod(duration_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        duration_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return duration_formatted

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
        fields = ["user", "track_id", "total_tracks"]

class CollectionPodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPods
        fields = ["user", "cast_id", "total_casts"]