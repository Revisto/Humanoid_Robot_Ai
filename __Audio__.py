import speech_recognition as sr
import random
import wikipedia 
from googletrans import Translator
import os
import random
from persiantools.jdatetime import JalaliDate
import khayyam
from time import sleep
from mpyg321.mpyg321 import MPyg321Player
from mutagen.mp3 import MP3
import feedparser
import mysql.connector as sql
import requests
from bs4 import BeautifulSoup
from math import sqrt
import sys
import numpy
import csv
from forecastiopy import *
#-----L I B R A R I E S-----
 
def MusicPlay(RareInput):
    MusicName,text=RareInput.split("()")
    print (MusicName,text)
    player = MPyg321Player()       # instanciate the player
    player.play_song(MusicName+".mp3") # play a song
    sleep(FindHowMuchToPlay(MusicName,text))               
    player.quit()  
def LenMusic(MusicNameNoDotMp3):

    audio = MP3(MusicNameNoDotMp3+".mp3")
    return audio.info.length
def FindHowMuchToPlay(MusicNameNoDotMp3,text):
    text=text.split(" ")
    Second=""
    for i in range (len(text)):
        try:
            text[i]=int(text[i])
            Second=int(text[i])
        except:
            None
    if Second=="":
        return LenMusic(MusicNameNoDotMp3)
    else:
        return Second
def Anthems(text="nothing"):
    list_en=["Poland","Russia","Soviet","United Kingdom","Brazil","Canada","France","Germany","Iran","Italy"]
    list_fa=[["لهستان"],["روسیه"],["شوروی"],["اینگیلیس","انگلیس","انگلستان","بریتانیا"],["برزیل"],["کانادا"],["فرانسه"],["آلمان","المان"],["ایران"],["ایتالیا"]]
    for Box in list_fa:
        for Little_Box in Box:

            if Little_Box in text:
                MusicPlay(list_en[list_fa.index(Box)]+"()"+text)
                return 
    
    TTS(random.choice(["پیدا نکردم","تو انبار نداریم"]),"fa")
def Analyse(text,DATA):
    Done=False
    for i in range (len(DATA)):
        if Done==True:
            break
        for Each_Question in DATA[i][0]:
            if str(Each_Question) in text:
                if DATA[i][1]!=[]:
                    TTS(str(random.choice(DATA[i][1])),"fa")
                if DATA[i][2]!=[]:
                    func=random.choice(DATA[i][2])
                    if len(func)>1:
                        func[0](random.choice(func[1:len(func)]))
                    else:
                        func[0]()
                Done=True
                break
    if Done==False:
        TTS(random.choice(["متاسفانه متوجهِ منظورتون نِمیشم","متاسفانه متوجه نَشدم","شرمنده متوجه منظورتون نِمیشم","شرمنده متوجهِ نشدم","من دارم یاد میگیرم و متوجهِ منظورتون نِمیشم","متاسفانه نفهمیدم"]),"fa")
def CompleteVoiceAnalyse():
    MusicPlay("Click"+"()"+"0.0")
    audio = GetVoice()
    MusicPlay("WaitAna"+"()"+"0.0")
    text = AnalyseVoice(audio)
    return text
def GetVoice():    
    mic = sr.Microphone()
    r=sr.Recognizer()
    with mic as source:
        audio = r.listen(source)
    return (audio)   
def AnalyseVoice(audio):
    mic = sr.Microphone()
    r=sr.Recognizer()
    text = r.recognize_google(audio, language='fa-IR')# language  set farsi :)
    return text
def MusicNames(name,num):
    List=[]
    for i in range (int(num)):
        List.append(str(name)+"_"+str(i+1))
    return List
def AllMusicsList():
    List=[MusicNames("BehnamBani",1)+MusicNames("HamedBahram",1)+MusicNames("AronAfshar",1)+MusicNames("Turkish",1)+MusicNames("Gypsy",1)+MusicNames("BabakJahanbakhsh",1)]
    return List[0]
def TTS_Offline(text,language):
    os.system("espeak -v "+'"'+str(language)+'"'+" "+'"'+str(text)+'"'+" "+"-s 20 -g 2")
def TTS(TEXT,fa):
    doc = requests.get("http://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=C6QAXK7BNFEI10M&Text="+TEXT+"&Speaker=Male1&Format=mp3&GainLevel=0&PitchLevel=0&PunctuationLevel=0&SpeechSpeedLevel=-10&ToneLevel=0&Quality=normal&BeginningSilence=0&EndingSilence=0&Base64Encode=0")
    with open('movie.mp3', 'wb') as f:
        f.write(doc.content)
    MusicPlay("movie"+"()کامل")
