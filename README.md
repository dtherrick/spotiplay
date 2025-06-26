Plan of attack:
1. Authenticate to get a token
2. load the playlist file: text into list of dicts
3. for each line:
    1. search for the song
    2. take the spotify URI of the track
4. Create the playlist
    1. Get the Spotify ID of the playlist
5. Create a comma separated list of the song URIs
6. Send the command to add tracks to the playlist.

[ ] restructure to see if you can link into the hypermodern design document
[ ] write this as a more generalized tool so you can build random playlists from large groups of songs.
