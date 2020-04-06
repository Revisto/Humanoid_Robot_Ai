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
from imp import reload
#-----L I B R A R I E S-----
from __Audio__ import *
from __Data__ import *
from __Date_Weather__ import *
from __Games__ import *
from __Others__ import *
from __Prices__ import *
from __TimingJobs__ import *
import ___DataBase___
#-----L  O  C  A   L-----

PricesInfo=GetSomeInfoAboutPrice()
TTS("در خدمتم","fa")

while True:
    reload(___DataBase___)
    #text=CompleteVoiceAnalyse()
    text = input("text=")
    if 'خاموش' in text:
        while 'روشن' not in text or 'بیدار' not in text:
            text=CompleteVoiceAnalysMute()

    elif WHQ(text) and text!="":
        Analyse_Closest(text,___DataBase___.DataBase)
    
    
    elif not(Analyse_Function(text,DATA_function(text,PricesInfo))) and text!="":
        AddToDataBase(text)
        #IDK() 

    elif text!="":
        AddToDataBase(text)



"""
 ██████╗  ███████╗ ██╗   ██╗ ██╗ ███████╗ ████████╗  ██████╗  
 ██╔══██╗ ██╔════╝ ██║   ██║ ██║ ██╔════╝ ╚══██╔══╝ ██╔═══██╗ 
 ██████╔╝ █████╗   ██║   ██║ ██║ ███████╗    ██║    ██║   ██║ 
 ██╔══██╗ ██╔══╝   ╚██╗ ██╔╝ ██║ ╚════██║    ██║    ██║   ██║ 
 ██║  ██║ ███████╗  ╚████╔╝  ██║ ███████║    ██║    ╚██████╔╝ 
 ╚═╝  ╚═╝ ╚══════╝   ╚═══╝   ╚═╝ ╚══════╝    ╚═╝     ╚═════╝ 
"""