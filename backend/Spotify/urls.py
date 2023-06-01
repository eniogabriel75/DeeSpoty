from django.urls import path, include
from Spotify import views
from rest_framework.routers import DefaultRouter

app_name = 'Spotify'

router = DefaultRouter()
router.register('spotify', views.SpotifyViewSet, basename='spotify')

urlpatterns = [
    path('', include(router.urls)),
    path('spotify/login/', views.SpotifyViewSet.as_view({'get': 'list'}), name='spotify-login'),
    path('spotify/callback/', views.SpotifyViewSet.as_view({'get': 'list'}), name='spotify-callback'),

]