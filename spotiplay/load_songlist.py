import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = 'playlist-modify-public'
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

str_pathfile = '/home/damian/Data/spotiplay/playlist.txt'
str_jsonfile = '/home/damian/Data/spotiplay/playlist.json'

file = open(str_pathfile, 'r')
tracks = file.readlines()

track_info = []
for track in tracks:
    tmp = {}
    tmp['search_string'] = track.strip()
    tmp['result'] = sp.search(track.strip(), type='track,artist')
    tmp['uri'] = tmp['result']['tracks']['items'][0]['uri']
    track_info.append(tmp)

with open(str_jsonfile, 'w') as outfile:
    json.dump(track_info, outfile)
