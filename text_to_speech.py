__author__ = 'Cyrus'
from gtts import gTTS
import time


def read(text):
     tts = gTTS(text=text, lang='en')
     filename = "tts_"+ str(time.time()) +".mp3"
     tts.save(filename)