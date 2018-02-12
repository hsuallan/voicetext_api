import requests
from requests.auth import HTTPBasicAuth
import pygame

class viocetext:
    _URL = 'https://api.voicetext.jp/v1/tts'#post request url
    _dict = {"text":"","speaker":"hikari","format":"mp3","emotion":"happiness","emotion_level":"2","pitch":"100","speed":"100","volume":"100"}#傳送的資料
    def __init__(self,api_key):
        self._auth = HTTPBasicAuth(api_key, api_key)
    def speak(self,text):
        self._dict["text"] = text
        self._get = requests.post(self._URL,data =self._dict ,auth=self._auth)
        self._tempfile = open("temp.mp3","wb",buffering = 1000000000)
        self._tempfile.write(self._get.content)
        self._tempfile.close()
        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()
    def set_speaker(self,speaker):
        print("")
    def set_emotion(self,emption):
        print("")
    def set_emotion_level(self,level):
        print("")
    def set_pitch(self,pitch):
        print()
    def set_speed(self,speed):
        print()
    def set_volume(self,vol):
        print()
    def save_as_wav(self,text):
        print()
a = viocetext("zkoiea4yphm49iyn")
a.speak("おはよう")
        


