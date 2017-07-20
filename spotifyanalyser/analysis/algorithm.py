import spotipy
import spotipy.util as util


class Track:
    def __init__(self, artists, title, date_added):
        self.artists = artists
        self.title = title
        self.date_added = date_added


class Playlist:
    """ An object for a spotify playlist """

    def __init__(self,name):
        self.playlist_name = name
        self.tracks = []
        pass

    def set_tracks(self, tracks):
        self.tracks = tracks

class Analyser:
    """ Analyse a playlist """
    def __init__(self, username):
        self.username = username
        scope = 'user-library-read'
        token = util.prompt_for_user_token(username,scope)
        self.spotify = spotipy.Spotify(auth=token)
        self.user_playlists = []
        self.scrape_playlist()
        for playlist in self.user_playlists:
            print(playlist.playlist_name + ' : ' + str(len(playlist.tracks)))

    def scrape_playlist(self):
        playlists = self.spotify.current_user_playlists()

        for playlist in playlists['items']:
            name = (playlist['name'])
            saved_playlist = Playlist(name)
            if playlist['owner']['id'].lower() == self.username.lower():
                print(playlist['name'])
                results = self.spotify.user_playlist(self.username, playlist['id'],
                                           fields="tracks,next")
                tracks = results['tracks']
                playlist_tracks = []
                for item in tracks['items']:
                    date = item['added_at']
                    artists = []
                    track = item['track']
                    song = track['name']
                    for artist in track['artists']:
                        artists.append(artist['name'])
                    saved_track = Track(artists,song,date)
                    playlist_tracks.append(saved_track)

                saved_playlist.set_tracks(playlist_tracks)
            self.user_playlists.append(saved_playlist)

if __name__ == '__main__':
    print("Started application")
    a = Analyser('Insanity0107')
