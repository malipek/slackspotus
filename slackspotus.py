import spotipy
from spotipy.oauth2 import SpotifyOAuth
import configparser
import os

env = 'PROD'

scope = "user-read-currently-playing"

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def authorize_spotify(config):
    os.environ['SPOTIPY_CLIENT_ID']=config[env]['spotifyclientid']
    os.environ['SPOTIPY_CLIENT_SECRET']=config[env]['spotifyclientsecret']
    os.environ['SPOTIPY_REDIRECT_URI']=config[env]['spotifyredirecturl']
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_current_track(config):
    spotify = authorize_spotify(config)
    current_track = spotify.current_user_playing_track()
    return current_track

def get_track_name(current_track):
    track_name = current_track['item']['name']
    return track_name

def get_track_artist(current_track):
    track_artist = current_track['item']['artists'][0]['name']
    return track_artist

def main():
    config=read_config()
    if not config:
        print('Error reading config')
        return
    track = get_current_track(config)
    print(get_track_artist(track)+': '+get_track_name(track))

if __name__ == '__main__':
    main()
