from django.urls import path
from MyApp import views

urlpatterns = [
    path('tracks/', views.TrackViewSet.as_view(), name='track-list'),
    path('playlists/', views.PlaylistViewSet.as_view(), name='playlist-list'),
    path('artists/', views.ArtistViewSet.as_view(), name='artist-list'),
    #path('colection/tracks/', views.CollectionViewSet.as_view(), name='collection-list'),
]