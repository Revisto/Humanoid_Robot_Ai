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
from __Audio__ import *
#-----L I B R A R I E S-----
 
def GetSomeInfoAboutPrice():
    url = "https://www.iranjib.ir/showgroup/23/realtime_price/"
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    return text
def RobCoin(text):
    TTS((text[(text.index("  ربع سکه"))+3])+"ریال","fa")
def HalfCoinPrice(text):
    TTS((text[(text.index("  نیم سکه"))+3])+"ریال","fa")
def FullCoinPrice(text):
    TTS((text[(text.index("  طرح جدید"))+3])+"ریال","fa")
def DollarPrice(text):
    TTS((text[(text.index("  قیمت دلار"))+3])+"ریال","fa")
def EuroPrice(text):
    TTS((text[(text.index("  قیمت یورو"))+3])+"ریال","fa")
def PondPrice(text):
    TTS((text[(text.index("  قیمت پوند انگلیس"))+3])+"ریال","fa")
def DerhamPrice(text):
    TTS((text[(text.index("  قیمت درهم"))+3])+"ریال","fa")
def LirPrice(text):
    TTS((text[(text.index("  قیمت لیر ترکیه"))+3])+"ریال","fa")
def GoldPrice(text):
    TTS((text[(text.index("  هر گرم طلای 18 عیار"))+3])+"ریال","fa")
def BitCoinPrice(text):
    PriceInDollar=((text[(text.index("  بیت کوین / Bitcoin"))+3]))
    PriceInDollar=PriceInDollar.split(".")
    PriceInDollar.append(0)
    First=PriceInDollar[0].split(",")
    All=""
    for i in First:
        All+=str(i)
    All=int(All)
    Doll=((text[(text.index("  قیمت دلار"))+3]))
    Doll=Doll.split(",")
    All_=""
    for i in Doll:
        All_+=str(i)
    All_=int(All_)
    Rial=All_*All
    TTS(str(Rial)+"ریال","fa")
