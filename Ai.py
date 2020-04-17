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
from ___Local___ import *
import ___DataBase___ 
#-----L  O  C  A   L-----


Audio().TTS("در خدمتم","fa")

while True:
    reload(___DataBase___)
    text=Audio().CompleteVoiceAnalyse()
    #text = input("text=")
    if 'خاموش' in text:
        while 'روشن' not in text or 'بیدار' not in text:
            text=Audio().CompleteVoiceAnalysMute()

    elif Data().WHQ(text) and text!="" and Data().Analyse_Closest(text,___DataBase___.DataBase):
        None
    
    
    elif not(Data().Analyse_Function(text,Data().DATA_function(text))) and text!="":
        Data().AddToDataBase(text)
        #IDK() 

    elif text!="":
        Data().AddToDataBase(text)



"""
 ██████╗  ███████╗ ██╗   ██╗ ██╗ ███████╗ ████████╗  ██████╗  
 ██╔══██╗ ██╔════╝ ██║   ██║ ██║ ██╔════╝ ╚══██╔══╝ ██╔═══██╗ 
 ██████╔╝ █████╗   ██║   ██║ ██║ ███████╗    ██║    ██║   ██║ 
 ██╔══██╗ ██╔══╝   ╚██╗ ██╔╝ ██║ ╚════██║    ██║    ██║   ██║ 
 ██║  ██║ ███████╗  ╚████╔╝  ██║ ███████║    ██║    ╚██████╔╝ 
 ╚═╝  ╚═╝ ╚══════╝   ╚═══╝   ╚═╝ ╚══════╝    ╚═╝     ╚═════╝ 
"""