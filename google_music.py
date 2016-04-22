from gmusicapi import Mobileclient
import config

config_dict = config.get_dict_of_params()
api = Mobileclient()
api.login(config_dict['gmail'], config_dict['gmail_password'], Mobileclient.FROM_MAC_ADDRESS)
# => True

library = api.get_all_songs()

def get_songs_by_artist(artist='Alice in Chains'):
    toPlay = [track['id'] for track in library
                       if track['artist'] == artist]
    return toPlay


def get_playlist_songs(playlist):
    return 0