# function.py houses all of the functions for Jarvis2.0

# imports
import datetime
import json
import time
import pyautogui
import spotipy
import subprocess
from spotipy.oauth2 import SpotifyOAuth
from selenium import webdriver
import googletrans
from googletrans import Translator
import os
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()

username = os.getenv("username")
clientID = os.getenv("clientID")
clientSecret = os.getenv("clientSecret")
# spotify api
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()


scope = 'user-read-playback-state user-modify-playback-state'
auth_manager = SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def check_time():
    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()

    # Calculate the time difference for GMT+8
    gmt_offset = datetime.timedelta(hours=8)

    # Add the offset to the UTC time
    local_time = utc_now + gmt_offset

    # Format the local time
    formatted_time = local_time.strftime('%H:%M:%S')

    print("It is " + formatted_time, "in Singapore right now, Sir.")

def quit_program():
    print("Shutting Down...")
    quit()

def pause_music():
    sp.pause_playback()

def skip_music():
    sp.next_track()

def play_track(song):
    device_id = get_active_device_id()
    results = sp.search(q=song, type='track')
    track_id = results['tracks']['items'][0]['id']
    if device_id:
        sp.transfer_playback(device_id=device_id, force_play=True)
        sp.start_playback(uris=['spotify:track:' + track_id])
    else:
        subprocess.run(['spotify'])
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(4)
        device_id = get_active_device_id()
        results = sp.search(q=song, type='track')
        track_id = results['tracks']['items'][0]['id']
        if device_id:
            sp.transfer_playback(device_id=device_id, force_play=True)
            sp.start_playback(uris=['spotify:track:' + track_id])

def get_active_device_id():
    devices = sp.devices()
    for device in devices['devices']:
        if device['is_active']:
            return device['id']
    return None

def search(search_query):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(f"https://www.google.com/search?q={search_query}")

def translate(text, start_language, end_language):
    translator = Translator()
    translated = translator.translate(text, src=start_language, dest=end_language)
    print(str(translated.text))