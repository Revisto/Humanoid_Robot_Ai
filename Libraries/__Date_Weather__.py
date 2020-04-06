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
from __Audio__ import *
#-----L I B R A R I E S-----
 
def Date():
    Months=["فَروَردین","اَردیبِهِشت","خُرداد","تیر","مُرداد","شَهریوَر","مِهر","آبان","آذَر","دِی","بَهمَن","اِسفَند"]
    Date=(JalaliDate.today())
    Date=str(Date).split("-")
    if str(Date[2])[0]=="0":
        Date[2]=Date[2][1]
    TTS("روزِ"+str(Date[2])+"اُمِ"+","+"ماهِ"+Months[(int(Date[1])-1)]+","+"سالِ"+str(Date[0]), "fa")
def Time_Now():
    time=(khayyam.JalaliDatetime.now().strftime('%C')).split(" ")
    time=(time[-2])
    time=time.split(":")
    for i in range (len(time)):
        time[i]=int(time[i])
        time[i]=str(time[i])
    TTS("ساعت"+time[0]+","+"ُّ"+","+time[1]+"دقیقِ"+"ُ"+","+time[2]+"ثانیه","fa")
def Day():
    time=(khayyam.JalaliDatetime.now().strftime('%C')).split(" ")
    day=time[-6]
    try:
        day=time[-7]+" "+day
    except:
        None
    TTS(day,"fa")
def Temperature(text):
    api_key = 'ccba47305cec42476fcbcc3b6892bd24'

    loc = [\
    ["Tehran, Iran", 35.6892, 51.3890 ],\
    ]
    for i in range(len(loc)):
        city=[]
        city.append(loc[i])
        weather = ForecastIO.ForecastIO(api_key, units=ForecastIO.ForecastIO.UNITS_SI,
                                        lang=ForecastIO.ForecastIO.LANG_ENGLISH, 
                                        latitude=loc[i][1], longitude=loc[i][2])
        current = FIOCurrently.FIOCurrently(weather)
        daily = FIODaily.FIODaily(weather)
        print(daily.summary)
        print(daily.icon)
        for day in range(2, 7):
            if day==2:
                TTS("امروز","fa")
            if day==3:
                TTS("فردا","fa")
            if day==4:
                TTS("پس فردا","fa")
            if day==5:
                TTS("سه روز بعد","fa")
            if day==6:
                TTS("چهار روز بعد","fa")

            val = daily.get(day)
            print (val)
            if "خلاصه" in text:
                Sum=(Translate((val['summary']),"fa"))
                if "نور" in Sum:
                    Sum=Sum.replace("نور","سبک")
                TTS (Sum,"fa")
            if "دما" in text or "هوا" in text:
                TTS (("کمترین دما",int(val['temperatureMin'] ),"درجه سانتی گِراد"),"fa")
                TTS (("بیشترین دما",int(val['temperatureMax'] ),"درجه سانتی گِراد"),"fa")
            if "سرعت" in text:
                TTS ((" سرعتِ باد",int(val['windSpeed'] ),"کیلومتر بر ساعت"),"fa")
            if "امروز" in text:
                break
            if "پس فردا" in text and day==3:
                break
