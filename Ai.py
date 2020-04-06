"""
 ███╗   ███╗  █████╗  ██╗ ███╗   ██╗ ██╗ 
 ████╗ ████║ ██╔══██╗ ██║ ████╗  ██║ ██║ 
 ██╔████╔██║ ███████║ ██║ ██╔██╗ ██║ ██║ 
 ██║╚██╔╝██║ ██╔══██║ ██║ ██║╚██╗██║ ╚═╝ 
 ██║ ╚═╝ ██║ ██║  ██║ ██║ ██║ ╚████║ ██╗ 
 ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝ 
"""


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
from __Audio__ import *
from __Data__ import *
from __Date_Weather__ import *
from __Games__ import *
from __Others__ import *
from __Prices__ import *
from __TimingJobs__ import *



PricesInfo=GetSomeInfoAboutPrice()
TTS("در خدمتم ","fa")
Status="Done"
while True:
    Status=WakeUp(TimeMustWakeUp,Time_Now_For_WakeUp(),Status)
    #RimindReminders(ReturnAllReminders(),Time_Now_For_WakeUp())
    try:
        text = CompleteVoiceAnalyse()
        if "بیدار" in text:
            TimeMustWakeUp=TimeMustWakeUp(text)
            print (TimeMustWakeUp)
            Status="NowNow"
        if "بیدار" not in text:
            if text!="" and "خاموش" not in text:
                print (text)
                Analyse(text,DATA_function(text,PricesInfo))  
            else:
                TTS("خاموش" , "fa")
                while "روشن" not in text:
                    Status=WakeUp(TimeMustWakeUp,Time_Now_For_WakeUp(),Status)
                    try:
                        audio = GetVoice()
                        text= AnalyseVoice(audio)
                    except Exception as Error:
                        print(Error)
    except Exception as Error:
        print(Error)


"""
 ██████╗  ███████╗ ██╗   ██╗ ██╗ ███████╗ ████████╗  ██████╗  
 ██╔══██╗ ██╔════╝ ██║   ██║ ██║ ██╔════╝ ╚══██╔══╝ ██╔═══██╗ 
 ██████╔╝ █████╗   ██║   ██║ ██║ ███████╗    ██║    ██║   ██║ 
 ██╔══██╗ ██╔══╝   ╚██╗ ██╔╝ ██║ ╚════██║    ██║    ██║   ██║ 
 ██║  ██║ ███████╗  ╚████╔╝  ██║ ███████║    ██║    ╚██████╔╝ 
 ╚═╝  ╚═╝ ╚══════╝   ╚═══╝   ╚═╝ ╚══════╝    ╚═╝     ╚═════╝ 
"""