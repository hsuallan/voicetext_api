import requests
from requests.auth import HTTPBasicAuth
import pygame

class viocetext:
    URL = 'https://api.voicetext.jp/v1/tts'
    data={"text":"","speaker":"hikari","format":"mp3","emotion":"happiness","emotion_level":"2","pitch":"100","speed":"100","volume":"100"}
    def __init__(self,api_key):
        self.auth = HTTPBasicAuth(api_key, api_key)
    def speak(self,text):
        print("")
    def speak(self,text,speaker):
        print("")
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


