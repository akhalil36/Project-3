from django.shortcuts import render, redirect
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def home(request):
    return render(request, 'home.html')

def login(request):
    sp_oauth = SpotifyOAuth(client_id='your_client_id',
                            client_secret='your_client_secret',
                            redirect_uri='your_redirect_uri',
                            scope='user-top-read')
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    else:
        return redirect('top_tracks')

def top_tracks(request):
    sp = Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                           client_secret='your_client_secret',
                                           redirect_uri='your_redirect_uri',
                                           scope='user-top-read'))
    results = sp.current_user_top_tracks(limit=10)
    context = {'tracks': results['items']}
    return render(request, 'top_tracks.html', context)

