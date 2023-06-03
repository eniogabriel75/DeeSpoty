import requests

class SpotifyService:
    CLIENT_ID = '2072f0a711994403a9680439e1757d85'
    CLIENT_SECRET = '1305bdd02aec40ceb0e001a5690a3206'
    REDIRECT_URI = 'https://127.0.0.1:8000//api/Spotify/services/callback/'

    @classmethod
    def get_authorize_url(cls):
        endpoint = 'https://accounts.spotify.com/authorize'
        params = {
            'client_id': cls.CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': cls.REDIRECT_URI,
            'scope': 'user-read-private user-read-email''playlist-read-private''playlist-read-collaborative''playlist-modify-private''playlist-modify-public'
            'user-read-playback-state''user-modify-playback-state''user-read-currently-playing''user-read-playback-position''user-top-read''user-read-recently-played'
            'user-library-modify''user-library-read''user-soa-link''user-soa-unlink''user-manage-entitlements''user-manage-partner''user-create-partner',  # Adicione as permissões necessárias
            }, 
        url = f'{endpoint}?{"&".join(f"{key}={value}" for key, value in params.items())}'
        return url

    @classmethod
    def get_access_token(cls, code):
        endpoint = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': cls.REDIRECT_URI,
            'client_id': cls.CLIENT_ID,
            'client_secret': cls.CLIENT_SECRET,
        }
        response = requests.post(endpoint, data=data)
        if response.status_code == 200:
            return response.json().get('access_token')
        return None