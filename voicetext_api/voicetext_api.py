import requests
from requests.auth import HTTPBasicAuth
import pygame

class viocetext:
    _URL = 'https://api.voicetext.jp/v1/tts'#post request url
    _dict = {"text":"","speaker":"hikari","format":"mp3","emotion":None,"emotion_level":None,"pitch":"100","speed":"100","volume":"100"}#傳送的資料
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
        self._dict["speaker"] = speaker
    def set_emotion(self,emption):
        self._dict["emption"] = emption
    def set_emotion_level(self,level):
        self._dict["emotion_level"] = level
    def set_pitch(self,pitch):
         if pitch>200:
            pitch = 200
         elif pitch< 50:
             pitch = 50
         self._dict["pitch"] = pitch
    def set_speed(self,speed):
        if speed>200:
            speed = 200
        elif speed<50:
            speed = 50
        self._dict["speed"] = speed
    def set_volume(self,vol):
        if vol>200:
            vol = 200
        elif vol<50:
            vol = 50
        self._dict["vol"] = vol
    def save_as_wav(self,text):
        self._dict["text"] = text
        self._dict["format"] = "wav"
        self._get = requests.post(self._URL,data =self._dict ,auth=self._auth)
        self._tempfile = open(text+".wav","wb",buffering = 1000000000)
        self._tempfile.write(self._get.content)
        self._tempfile.close()
        print("successfully save as"+text+".wav")



        


