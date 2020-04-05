import requests
from mpyg321.mpyg321 import MPyg321Player
import time
TEXT=input("متن فارسی :")
doc = requests.get("http://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=C6QAXK7BNFEI10M&Text="+TEXT+"&Speaker=Female1&Format=mp3")
with open('movie.mp3', 'wb') as f:
    f.write(doc.content)
player = MPyg321Player()       # instanciate the player
player.play_song("movie.mp3") # play a song
time.sleep(5)