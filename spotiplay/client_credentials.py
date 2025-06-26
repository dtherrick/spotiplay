import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('dtherrick', limit=15, offset=5)

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(f"{playlist['name']}, {playlist['uri']}")
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
