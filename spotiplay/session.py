import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']

scope = "user-library-read"

auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope)

auth_url = auth_manager.get_authorization_code()
print(f'Visit: {auth_url}')
# code = input('Enter the authorization code: ')

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.current_user_saved_tracks(limit=10, offset=5)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx}. {track['artists'][0]['name']} - {track['name']}")
