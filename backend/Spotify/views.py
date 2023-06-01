from rest_framework import viewsets
from rest_framework.response import Response
from Spotify.services import SpotifyService

class SpotifyViewSet(viewsets.ViewSet):
    def login(self, request):
        redirect_url = SpotifyService.get_authorize_url()
        return Response({'redirect_url': redirect_url})

    def callback(self, request):
        code = request.GET.get('code')
        access_token = SpotifyService.get_access_token(code)
        if code is none:
             return Response({'error': 'Missing code parameter'}, status=status.HTTP_400_BAD_REQUEST)
        if access_token:
            # Salvar ou utilizar o access_token conforme necessário
            return Response({'access_token': access_token},status=status.HTTP_200_OK)
        else:
            # Lógica de tratamento para falha na obtenção do access_token
            return Response({'error': 'Failed to obtain access token'}, status=status.HTTP_400_BAD_REQUEST)

"""class DeezerViewSet(viewsets.ViewSet):
    def login(self, request):
        redirect_url = DeezerService.get_authorize_url()
        return Response({'redirect_url': redirect_url})

    def callback(self, request):
        code = request.GET.get('code')
        access_token = DeezerService.get_access_token(code)
        if access_token:
            # Salvar ou utilizar o access_token conforme necessário
            return Response({'access_token': access_token})
        else:
            # Lógica de tratamento para falha na obtenção do access_token
            return Response({'error': 'Failed to obtain access token'})"""