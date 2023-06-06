from django.urls import path
from MyApp import views

urlpatterns = [
    path('tracks/', views.TrackViewSet.as_view(), name='track-list'),
    path('playlists/', views.PlaylistViewSet.as_view(), name='playlist-list'),
    path('artists/', views.ArtistViewSet.as_view(), name='artist-list'),
    path('albums/', views.AlbumViewSet.as_view(), name='album-list'),
    path('creators/', views.CreatorViewSet.as_view(), name='creators-list'),
    path('podcasts/', views.PodCastsViewSet.as_view(), name='podcasts-list'),
     path('collectiontracks/', views.CollectionTracksViewSet.as_view(), name='collectiontrack-list'),
    path('collectionpods/', views.CollectionPodsViewSet.as_view(), name='collectionpods-list'),
]