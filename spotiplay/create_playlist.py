import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def search_dict(list_of_dicts, playlist):
    res = next((sub for sub in list_of_dicts if sub['name'] == playlist), None)
    return res


def get_playlist_id(playlist, username, description=None):
    result = sp.current_user_playlists()
    filtered_res = search_dict(result['items'], playlist)

    if not filtered_res:
        sp.user_playlist_create(user=username,
                                name=playlist,
                                description=description)
        result = sp.current_user_playlists()
        filtered_res = search_dict(result['items'], playlist)

    pid = filtered_res['id']
    return pid


sourcefile = '/home/damian/Data/spotiplay/playlist.json'

username = 'dtherrick'
scope = "playlist-modify-public"
playlist_name = 'Memorial Playlist - Donna'
desc = 'Tracks selected to play during the memorial service on August 3, 2024'

f = open(sourcefile)
playlist_data = json.load(f)

uri_values = [d['uri'] for d in playlist_data]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlist_id = get_playlist_id(playlist=playlist_name,
                              username=username,
                              description=desc)

sp.playlist_add_items(playlist_id=playlist_id, items=uri_values)
