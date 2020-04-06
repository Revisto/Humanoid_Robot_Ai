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
 
def Game_Name(List):

    MusicPlay("Click"+"()"+"0.0")
    Input=GetVoice()
    MusicPlay("WaitAna"+"()"+"0.0")
    Input=AnalyseVoice(Input)
    if Input in List:
        List.remove(Input)
    else:
        TTS("دوباره امتحان کن , یک اسم بگو","fa")
        MusicPlay("Click"+"()"+"0.0")
        Input=GetVoice()
        MusicPlay("WaitAna"+"()"+"0.0")
        Input=AnalyseVoice(Input)
        if Input in List:
            List.remove(Input)
        else:
            return
    while True:

        TheLetter=Input[len(Input)-1]
        while True:
            name=random.choice(List)
            if name[0]==TheLetter:
                MyName=name
                break
        List.remove(MyName)
        TTS (MyName,"fa")
        MusicPlay("Click"+"()"+"0.0")
        Input=GetVoice()
        MusicPlay("WaitAna"+"()"+"0.0")
        Input=AnalyseVoice(Input)
        if Input in List and Input[0]==MyName[len(MyName)-1]:
            List.remove(Input)
        else:
            TTS("دوباره تلاش کن","fa")
            TTS(MyName,"fa")
            MusicPlay("Click"+"()"+"0.0")
            Input=GetVoice()
            MusicPlay("WaitAna"+"()"+"0.0")
            Input=AnalyseVoice(Input)
            if Input in List and Input[0]==MyName[len(MyName)-1]:
                List.remove(Input)
            else:
                TTS("شما باختی","fa")
                return
def calculating_game():
    def Is_numeric(Text):
        if Text.isnumeric()==True:
            return True
        elif Text[0]=="-":
            TEXT=Text.replace("-","")
            return TEXT.isnumeric()
        else:
            return False

    list_operators=["به علاوه","منهای","ضرب در"]
    level=1
    con=True
    while con==True:
        Text="حاصل"
        for i in range(level):
            Text+=" "+str(random.randint(1,9))+" "+random.choice(list_operators)
        Text+=" "+str(random.randint(1,9))
        TTS("شروع","fa")
        TTS(Text,"fa")
        Input=CompleteVoiceAnalyse()
        while Is_numeric(Input)==False:
            if Input=="تمام":
                con=False
                return 0
            else:
                TTS("دوباره بگو")
                Input=CompleteVoiceAnalyse()
        if calculater(Text)==int(Input):
            TTS("درسته","fa")
            level+=1
        else:
            TTS("غلطه","fa")
def reverse_True_and_False():
    list_questions=["آیا شما انسان هستید","یا بستنی داغ است","آیا زمین تخت است","آیا خورشید بنفش است","آیا جنگ خوب است","آیا فوتبال ورزش است","آیا قم کشور است","آیا فیل کوچک است","آیا ویروس بزرگ است","آیا رضا شاه وزیر بود","آیا شاهزاده وزیر است","آیا ماه ستاره است","آیا عراق شهر است","آیا پسر پدر وزیر پدرش است","آیا برج میلاد برج است","آیا شیر سیاه است","آیا سیاه روشن است","آیا خوبی بدی است","آیا اروپا کشور است","آیا بحرین بزرگ است","آیا آهن از پنبه سبک تر است"]
    key="nyyyynyyyyynyynyyyyyy"
    while True:
        Ind=random.randint(0,len(list_questions)-1)
        TTS(list_questions[Ind],"fa")
        iinput=CompleteVoiceAnalyse()
        if iinput=="بله":
            if key[Ind]=="y":
                TTS("درسته","fa")
            else:
                TTS("غلطه","fa")
        if iinput=="خیر":
            if key[Ind]=="n":
                TTS("درسته","fa")
            else:
                TTS("غلطه","fa")
        else:
            break
