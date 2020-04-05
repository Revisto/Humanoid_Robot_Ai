"""
 ██████╗  ███████╗ ███████╗ ██╗ 
 ██╔══██╗ ██╔════╝ ██╔════╝ ██║ 
 ██║  ██║ █████╗   █████╗   ██║ 
 ██║  ██║ ██╔══╝   ██╔══╝   ╚═╝ 
 ██████╔╝ ███████╗ ██║      ██╗ 
 ╚═════╝  ╚══════╝ ╚═╝      ╚═╝ 
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
def Joke():
    jokes=['  دیدی درد نداشت؟        جمله نوستالژیک پدر و مادرها بعد آمپول زدن به بچه هاشون در حالی که بچه داره خون گریه میکنه     یعنی اون همه اشک ماله شوق بوده.', ' کار بابام از کولر گذشته       دیگه شبا بلند میشه میاد مودم رو خاموش میکنه!.', ' دکمه روشن کنترلو 20 بار می زنی تلویزیون روشن نمی شه     عصبانی می شی، 2 بار پشت سر هم محکم فشار می دی روشن می شه دوباره خاموش می شه!', ' دیگه به درجه ای از عرفان رسیدم که واسه خودم یه چیزی تعریف می کنم می خندم   تازه آخرش هم از خودم می پرسم جان من؟!', ' یکی از محاسبه هایی که سریع انجام می دیم، محاسبه فاصله من و دادشم و خاهرم نسبت به آیفونه وقتی یکی زنگ درو می زنه!', ' روزگارا که چنین سخت به من می گیری با خبر باش که خیلی داری سخت می گیری دیگه! مسخرشو درآوردی', ' از جلوی یه رستوران رد میشدم دیدم روی درش نوشته: لورل بیا هاردی برو!', ' امروز دست خط خودمو بردم دارو خونه …        بهم دارو داد !', ' یارو ميره تو صف نونوايي، شاطر نونوائی ميگه: نون تا اينجا بيشتر نميرسه، بقيه برن. ميگه: ببخشيد اگه ميشه جمعتر وايسين نون به ما هم برسه', ' اگه میشد دانشمندا یه وسیله اختراع میکردند که از خروپوف برق تولید کنه الان بابام یه نیروگاه هسته ای محسوب می شد !.', ' تا حالا دقت کردین کسایی که خروپف میکنن ،  زودتر خوابشون میبره !؟', ' رفتم دادگستری یارو میپرسه شکایت داشتید؟ گفتم پـَـــ نــه پـَـــ یه خورده برنج آوردم با ترازوی عدالت وزن کنم !.', '  رفتم باغ وحش از نگهبانه میپرسم ببخشید آقا قفس شیرا کجاست ؟ میگه بازدید کننده ای پـَـــ نــه پـَـــ نه از اقوامشون هستم اینورا کاری داشتم گفتم سری بهشون بزنم', '  اومدم در یخچالو باز میکنم دنبال غذا مامانم میگه گشنته؟ پـَـــ نــه پـَـــ اومدم ببینم کی هی چراغ این تو رو خاموش روشن می کنه!.', ' یه بیماری هست اسم نداره اما نتیجه ش     نگهداشتن شیشه عطرها و اسپری های تموم شده ست !.', ' ﺑﻪ ﺑﻌﻀﯽ ﻫﺎ ﺑﺎﻳﺪ ﺑﮕﯽ :  ﺍﮔﻪ ﻭﺍﺳﻪ ﻫﻤﻪ ﻗﺎﻃﯽ ﭘﺎﺗﯽ ﻣﻴﮑﻨﯽ ، ﻭﺍﺳﻪ ﻣﺎ ﻫﻨﻮﺯ ﺗﺎﺗﯽ ﺗﺎﺗﯽ ﻣﻴﮑﻨﯽ !.', ' بدترین چیز اون خنده ی اجباری برای حفظ آبرو بعد از یه زمین خوردن وحشتناکه', ' بعضیا واسه همــه اقیانوس آرام هستن اما تا به ما میرسن میشن تنگهء هرمز!', ' فکر کنم رمز موفقیتمو ۳ بار اشتباه زدم قفل شده ', ' یه وقتایی لازمــه از گوشیمون بشنویم “مشترک مورد نظر آدم نمیباشد … لـــطفا قطع کنید”!', ' امسال نمایشگاه کتاب نرفتم ، خودم تو خونه سیب زمینی سرخ کردم خوردم !', ' زندگی مثل شطرنج میمونه ، البته تو که بچه ای برو منج بازی کن !', ' باهمه وجودم سرمو روشونه مهربون تو میذارم و یواشکی دماغمو با لباست پاک میکنم!!', ' خیلی دلم برات تنگ شده…اونقدر که از دوریت گریه ام میگره… اما وقتی قیافت یادم میاد خندم میگیره!!', ' افتخار نکن که به اندازه تار موهات رفیق داری. وقتی محتاجشون میشی می فهمی که کچلی.', ' وقتی مو تو غذا باشه،فرقی نداره مژه ی دلبر باشه یا سیبیل اصغر آقا!', ' این دهه ۶٠یا که هی نسل سوخته نسل سوخته میکنن   فکر نکنن ما یادمون رفته ماه رمضوناشون تو زمستون بوده ..!', ' جمله ای که من هروقت یه آدم پولدار میبینم واسه آروم کردن خودم میگم: آرامشی که ما داریمو اونا ندارن!!', ' میدونم یکی هست که تو دلش وِلولـس واسه خواستنــم فقط نمیدونم کجاست؟', ' بچه که بودم فکر میکردم زمان قدیم همه جا سیاه سفید بوده', ' بابام ﻣﯿﮕﻪ ﺍﻭﻝﮔﻮﺵ ﮐﻦ ﺑﺒﯿﻦ ﭼﯽ ﻣﯿﮕﻢ     ﺑﻌﺪ ﯾﺎ ﻗﺒﻮﻝ ﮐﻦﯾﺎ ﺑﺮﻭ ﻓﮑﺮﺍﺗﻮ ﮐﻦ ﺑﻌﺪ ﻗﺒﻮﻝ ﮐﻦ !', ' اومدم خونه به مامانم میگم گشنمه، میگه عزیزم نون هس ،تخم مرغ هس، روغنم هس،  برو هر چى دوس دارى درست کن بخور!', ' دو ماهه دارم هر شش ساعت یه بار دوتا آنتی هیستامین میندازم تو جیبام    ولی بازم جیب ما به پول حساسیت داره!', ' یه وختایی نمیرم دمه یخچال که پیشه من شرمنده نشه... خدا هیچ یخچالی رو شرمنده صاحبش نکنه.', ' دیگه کار از کلیپس گذشته برخی از دخترا در حال ساخت مسکن مهر رو سرشون هستند…!', '  اگه قرار باشه اون دنیا تو بهشت موسیقی های خوب گوش کنیم، فک کنم تو جهنم تتلو پخش کنن ', ' من حتی اگه بمیرم مامانم میاد سر قبرم میگه ببین بچه ی فلانی نصف توعه ولی زنده است ', ' پارسال با بابام دعوام شد بهش گفتم بالاخره یه روز از این خونه میرم الان یک ساله هر روز موقع شام و نهار میگه به به, شما که هنوز نرفتی.', '  دوستان نگران نباشید ویروس کرونا زود خراب میشه میمیره چون جنسش چینیه ', '  انقدر که توی سایت ها ربات نبودنمو ثابت کردم توی زندگیم آدم بودنمو ثابت نکردم ', '  دلم برای روزایی که تو دبستان با بچه ها دعوامون میشد کیفشو برمیداشتم پرت کنم میگف ننننددداااازززقران توشه تنگ شده... ', ' هم عاشقتم , هم ازت متنفرم , میانگین که بگیری میبینی برام مهم نیستی !', ' به سلامتی پنگوئن که یه ذره قد داره، اما بازم لاتی راه میره ….', ' بزرگترین حرف های کینه توزانه با این جمله توجیه میشه : ” به خاطر خودت میگم “', ' یه شلغمم نشدیم یکی کوفتمون کنه خوب شه…..!!', ' یه کتابم نشدیم حداقل دوست مهربان بشیم !!', ' طنز بگو', ' حیف نون به باباش میگه : پنکه خراب شدهباباش میگه : خوب معلومه پنج نفری زیرش میخوابین ، میخوای خراب نشه ؟!!', ' ه حیف نون میگن این خیابون کجا میره ؟میگه من ۴۰ ساله تو این خیابون زندگی میکنم تا حالا ندیدم جایی بره !', ' احساسی که با خنده همراه است.']
    TTS(random.choice(jokes),"fa") 
def Calculater(text):
    #print(text)
    #analizing part
    l_operations=[]
    l_names=[["تقسیم","/"],["ضرب","*"],["جمع","هوالع","علاوه","مجموع","+"],["منفی","منهای","-"]]
    #,["توان"],["رادیکال"]
    l_numbers=[]
    text=text.split()
    for item in text:
        if item.isnumeric()==True:
            l_numbers.append(int(item))
        for lis in l_names:
            if item in lis:
                l_operations.append(lis[-1])
    l_full=[]
    for i in range(len(l_operations)):
        l_full.append(l_numbers[i])
        l_full.append(l_operations[i])
    l_full.append(l_numbers[-1])
    #print(l_full)
    while "*" in l_full or "/" in l_full:
        ind_1=100
        ind_2=100
        if "*" in l_full:
            ind_1=l_full.index("*")
        if "/" in l_full:
            ind_2=l_full.index("/")
        ind=min(ind_1,ind_2)
        num_1=l_full[ind-1]
        num_2=l_full[ind+1]
        sum=0
        if l_full[ind]=="*":
            sum=int(num_1*num_2)
        else:
            sum=int(num_1/num_2)
        l_full.pop(ind)
        l_full.pop(ind)
        l_full.pop(ind-1)
        l_full.insert(ind-1,sum)
    while "+" in l_full or "-" in l_full:
        ind_1=100
        ind_2=100
        if "+" in l_full:
            ind_1=l_full.index("+")
        if "-" in l_full:
            ind_2=l_full.index("-")
        ind=min(ind_1,ind_2)
        num_1=l_full[ind-1]
        num_2=l_full[ind+1]
        sum=0
        if l_full[ind]=="+":
            sum=int(num_1+num_2)
        else:
            sum=int(num_1-num_2)
        l_full.pop(ind)
        l_full.pop(ind)
        l_full.pop(ind-1)
        l_full.insert(ind-1,sum)
    TTS(l_full[0],"fa")
def GoldPrice(text):
    TTS((text[(text.index("  هر گرم طلای 18 عیار"))+3])+"ریال","fa")
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
def GetSomeInfoAboutPrice():
    url = "https://www.iranjib.ir/showgroup/23/realtime_price/"
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    return text
def News(category):
    def parse_rss(rss_url):
        return feedparser.parse(rss_url)
    def get_headlines(rss_url):
        headlines = []
        feed = parse_rss(rss_url)
        for newsitem in feed['items']:
            headlines.append(newsitem['title'])

        return headlines
    allheadlines = []

    def start_db(host, user, passwd, db_name):
        conn = sql.connect(
            host="localhost",
            user="root",
            passwd="7221974",
        )
    for key, url in (category).items():
        allheadlines.extend(get_headlines(url))
    #f= open("news.txt","w")
    News=[]
    for hl in allheadlines:
        #f.write(str(hl)+"\n")
        #TTS(hl,"fa")
        News.append(hl)
    SelectedNews=[]
    for i in range (3):
        s=random.choice(News)
        SelectedNews.append(s)
        News.remove(s)
    for New in SelectedNews:
        TTS(New,"fa")
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
def Translate(text,translated_language):    #return translated text
    translator = Translator()
    result = translator.translate(str(text), dest=str(translated_language))
    translated=result.text
    return translated
def TTS(text,language):
    os.system("espeak -v "+'"'+str(language)+'"'+" "+'"'+str(text)+'"'+" "+"-s 20 -g 2")
def Search(text):
    def WhatToSearch(text):
        SplitText=text.split(" ")
        try:
            SplitText.remove("جستوجو")
        except :
            None
        try:
            SplitText.remove("جستجو")
        except :
            None
        try:
            SplitText.remove("جست")
        except :
            None
        try:
            SplitText.remove("جو")
        except :
            None
        try:
            SplitText.remove("سرچ")
        except :
            None
        try:
            SplitText.remove("کن")
        except :
            None
        try:
            SplitText.remove("بکن")
        except :
            None
        try:
            SplitText.remove("درباره")
        except :
            None
        try:
            SplitText.remove("را")
        except :
            None
        try:
            SplitText.remove("رو")
        except :
            None
        Output=""
        for i in SplitText:
            Output+=(str(i)+" ")
        return Output
    text=WhatToSearch(text)
    
    wikipedia.set_lang("fa")  
    suggestions=(wikipedia.search(text, results=1))
    suggestion =(suggestions[0])
    a=(wikipedia.summary(suggestion, sentences=2))  
    TTS(a,"fa") 

    try:
        text=""
        r=sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            audio = r.listen(source)
        return ("Checking")
        text = r.recognize_google(audio, language='fa-IR')# language  set farsi :)
        return str(text)
    except:
        return ""
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
def Time_Now_For_WakeUp():
    time=(khayyam.JalaliDatetime.now().strftime('%C')).split(" ")
    time=(time[-2])
    time=time.split(":")
    for i in range (len(time)):
        time[i]=int(time[i])
        time[i]=str(time[i])
        
    return [int(time[0]),int(time[1])]  
def TimeMustWakeUp(RareTime):
    while True:
        RareTime=RareTime.split(" ")
        Times=[]
        for i in range (len(RareTime)):
            try:
                Times.append(int(RareTime[i]))
            except:
                None
        if len(Times)!=2:
            TTS("ورودی اشتباه","fa")
            MusicPlay("Click"+"()"+"0.0")
            audio = GetVoice()
            MusicPlay("WaitAna"+"()"+"0.0")
            RareTime= AnalyseVoice(audio)
            print (RareTime)
        else:
            return Times
            break
def WakeUp(TimeMustWakeUp,Time,Status):          #return true flase         Time must be [12,13]   Time Must be [10,11]           TimeMustWakeUp-if input=none    return time   else change it
    if Status=="Done":
        return "Done"
    else:
        if ((int(Time[0])*60+int(Time[1]))-(int(TimeMustWakeUp[0])*60+int(TimeMustWakeUp[1])))<=10 and Status=="NowNow":
            MusicPlay("Calm"+"()20")
            return "Done"
        else:
            return "NotNow"
def ReturnAllReminders():
    All=[]
    Box=[]
    for i in (Reminders.read()).split(","):
        Box.append(i)
        if len(Box)==4:
            All.append(Box)
            Box=[]
    return All
def AddToReminder():
    TTS("اسمِ دارو","fa")
    MusicPlay("Click"+"()"+"0.0")
    audio=GetVoice()
    MusicPlay("WaitAna"+"()"+"0.0")
    name=AnalyseVoice(audio)
    while True:
        try:
            TTS("ساعتِ","fa")
            MusicPlay("Click"+"()"+"0.0")
            audio=GetVoice()
            MusicPlay("WaitAna"+"()"+"0.0")
            hour=AnalyseVoice(audio)
        except:
            None
        try:
            hour=int(hour)
            break
        except:
            None
    while True: 
        try:
            TTS("دقیقه یِ","fa")
            MusicPlay("Click"+"()"+"0.0")
            audio=GetVoice()
            MusicPlay("WaitAna"+"()"+"0.0")
            minute=AnalyseVoice(audio)
        except:
            None
        try:
            minute=int(minute)
            break
        except:
            None
        
    AllStr=""
    All=ReturnAllReminders()
    print (All)
    for Box in All:
        for little_box in Box:
            AllStr+=(str(little_box)+",")
    print (AllStr)
    AllStr+=name+","+str(hour)+","+str(minute)+","+"True"
    Reminders.seek(0)
    Reminders.truncate(0)
    Reminders.write(AllStr)
    print (AllStr)
    TTS("انجام شد","fa")
def DeleteFromReminder():
    Found=False
    All=ReturnAllReminders()   
    while True:
        TTS("اسم دارو","fa")
        MusicPlay("Click"+"()"+"0.0")
        audio=GetVoice()
        MusicPlay("WaitAna"+"()"+"0.0")
        name=AnalyseVoice(audio)
        TTS("ساعت","fa")
        MusicPlay("Click"+"()"+"0.0")
        audio=GetVoice()
        MusicPlay("WaitAna"+"()"+"0.0")
        hour=AnalyseVoice(audio)
        print (All)
        
        for i in range(len(All)):
            if All[i][0]==name and All[i][1]==hour:
                All.pop(i)
                Found=True
                break
        if Found==False:
            TTS("دوباره امتحان کن","fa")
        if Found==True:
            break
    TTS("انجام شد","fa")
    AllStr=""
    for Box in All:
        for little_box in Box:
            AllStr+=(str(little_box)+",")
    AllStr=AllStr[0:-1]
    Reminders.seek(0)
    Reminders.truncate(0)
    Reminders.write(AllStr)
def RimindReminders(MainListOfRiminds,Time):
    for Box in MainListOfRiminds:
        if Box[3]=="False":
            if ((int(Time[0])*60+int(Time[1]))-(int(Box[1])*60+int(Box[2])))>10 or ((int(Time[0])*60+int(Time[1]))-(int(Box[1])*60+int(Box[2])))<-10: 
                MainListOfRiminds[MainListOfRiminds.index(Box)][3]="True"             
        else:
            if ((int(Time[0])*60+int(Time[1]))-(int(Box[1])*60+int(Box[2])))<=10 and ((int(Time[0])*60+int(Time[1]))-(int(Box[1])*60+int(Box[2])))>0:
                TTS(Box[0],"fa")
                MainListOfRiminds[MainListOfRiminds.index(Box)][3]="False"
    Reminders.seek(0)  
    Reminders.truncate(0)
    AllStr=""
    for Box in MainListOfRiminds:
        for little_box in Box:
            AllStr+=(str(little_box)+",")
    Reminders.write(AllStr)
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
def DATA_function(text,PricesInfo):
    Game_List=['صالحه', 'یاسمن', 'لطیفه', 'مهشید', 'نازیلا', 'صدرا', 'برنامه', 'شاهرخ', 'هیراد', 'حمیده', 'بهزاد', 'کرم', 'نبی', 'ارغوان', 'احمد', 'اسما', 'ثمین', 'ساحره', 'مريم', 'مرسل', 'محمدعلی', 'ایلیا', 'رشید', 'واصف', 'حلیمه', 'رافع', 'مریم', 'فردین', 'آریا', 'فريد', 'رضیه', 'آصف', 'کمیل', 'آیین', 'مهراب', 'هوتن', 'سوده', 'عمار', 'محمد', 'رضابابایی', 'محمودرضا', 'فرهمند', 'جاوید', 'هاتف', 'رعنا', 'اقبال\u200cعلی', 'سیده', 'کاکا', 'مظاهر', 'خشایار', 'بشیر', 'ریاض', 'شکوه', 'کامین', 'یوسفعلی', 'صبریه', 'درنا', 'پگاه', 'اكبر', 'مبارک', 'پروانه', 'حوریه', 'عطاء', 'زائر', 'نیره', 'نويد', 'فرهنگ', 'نجیبه', 'طارق', 'شمس\u200cالدین', 'مصلح', 'فضیل', 'امیرحسن', 'برزو', 'كامران', 'اکبر', 'سجاد', 'نرگس', 'ناهيد', 'فرزاد', 'شادي', 'طوبی', 'علا', 'اویس', 'غمزه', 'نجمه', 'ستايش', 'ضیا\u200cالدین', 'صمیم', 'عابده', 'ناديا', 'آیدین', 'ثامر', 'سبحان', 'میثم', 'صانع', 'غزاله', 'شراره', 'افسانه', 'سينا', 'عاصم', 'عبدالرفیع', 'محمدصادق', 'حنیفه', 'رحمان', 'ابوالقاسم', 'وحیده', 'زانیار', 'ریحانه', 'عاقله', 'زین\u200cالدین', 'محمدسالار', 'حسن', 'منیر', 'یحیی', 'عهدیه', 'سروش', 'فربد', 'عاطفه', 'کاوه', 'عبدالحسن', 'ابوذر', 'طیبه', 'ساره', 'رضوان', 'عزیزالله', 'شهاب\u200cالدین', 'جمال', 'شروین', 'ستار', 'صنعان', 'طناز', 'میلان', 'صیاد', 'قادر', 'متینه', 'رایحه', 'سیمین', 'صنم', 'زاهر', 'لبیب', 'سلما', 'تهمینه', 'میلانا', 'محسن', 'عباس', 'نادیا', 'آیهان', 'شمیس', 'عبدالهادی', 'امید', 'فروز', 'صاحب', 'فرزام', 'صدف', 'توفیق', 'زینب', 'عطیه', 'زهرا', 'حسانه', 'مطهره', 'مهدا', 'فریناز', 'علی\u200cرضا', 'شاکر', 'سوگند', 'دیوید', 'پویا', 'حنانه', 'منظر', 'امیرپارسا', 'عزالدین', 'وهاب', 'زاهده', 'محمدحسین', 'اميرمحمد', 'عادل', 'بدری', 'نیلوفر', 'رسول', 'سهراب', 'طاها', 'میسان', 'اسماء', 'صداقت', 'شیرین', 'نرجس', 'مرسا', 'ندیم', 'صبا', 'سینا', 'محمدامین', 'مولود', 'اعظم', 'عالیه', 'عبدالرسول', 'دیاکو', 'ﺣﺴﻴﻦ', 'سیروس', 'جنید', 'کامل', 'لطیف', 'مسیب', 'ترمه', 'رزان', 'محترم', 'مختار', 'فرحان', 'مهدیار', 'عبدالعزیز', 'حامد', 'غیاث', 'سعید', 'فصیح', 'مرجان', 'آيه', 'خاطره', 'یاسمین', 'زکی', 'رحیمه', 'خضر', 'مهنا', 'علی\u200cمراد', 'ساسان', 'فیاض', 'مجیرالدین', 'امیر', 'اسماعیل', 'نیما', 'اذين', 'عبدالقادر', 'یعقوب', 'حبیبه', 'یزدان', 'میلاد', 'حسين', 'ساحل', 'عبدالحی', 'صادقه', 'مطیب', 'نادی', 'حامی', 'نریمان', 'شعبان', 'میترا', 'ایوب', 'نازنین', 'سمین', 'سلیم', 'شادی', 'آرین', 'کورش', 'هما', 'رفیعه', 'عقیل', 'عین\u200cالدین', 'مظفر', 'عبدالغفور', 'فرج', 'آبدین', 'صفا', 'ب', 'نيما', 'مهتا', 'اروین', 'سمیرا', 'میثاق', 'یاشار', 'واران', 'عبداللطیف', 'یدالله', 'مهرنوش', 'ستیلا', 'ساعده', 'فرشيد', 'سلوی', 'حیفا', 'مدینه', 'قاهر', 'َآرش', 'شیوا', 'بهجت', 'شکیل', 'فایزه', 'فرشید', 'سمیه', 'وریا', 'سامان', 'شهباز', 'کوروش', 'محمدمحسن', 'فتاح', 'غفور', 'نورالدین', 'دانیال', 'مهندس', 'ساجده', 'نصر', 'میوند', 'کسری', 'مصباح', 'طاهر', 'نگار', 'روح', 'فرحانه', 'ربیع', 'واهب', 'آنسه', 'رحمت', 'کریمه', 'پریساحسین', 'ترنم', 'آلاء', 'عمید', 'سرور', 'پرستو', 'رستم', 'خیزران', 'صادق', 'امين', 'شیدا', 'ربابه', 'اميرحسين', 'نادره', 'امیررضا', 'محفوظ', 'شبلی', 'عبدالحق', 'مجیر', 'مهام', 'عبدالمجید', 'بابک', 'آقای', 'نهال', 'طه', 'عبدالواحد', 'میسا', 'مبین', 'حمزه', 'سمیه.', 'مهری', 'همام', 'آروين', 'سهیلا', 'زکیه', 'مونس', 'عبدالصمد', 'برهان', 'سحاب', 'تبسم', 'توحید', 'ماهر', 'رایموند', 'بهاره', 'فریعد', 'کبری', 'امیرپوریا', 'گیلدا', 'رضی', 'طالب', 'اشکان', 'حارثه', 'بشرا', 'رابعه', 'محبوبه', 'عابس', 'کمال', 'نعیمه', 'ماه', 'مهشيد', 'شادمان', 'شایان', 'اوبالیت', 'اللهیار', 'فاطر', 'اوحد', 'کیسان', 'آبد', 'صلاح\u200cادین', 'عمرو', 'مجتبي', 'فرح', 'شکرالله', 'مرتضی', 'علی\u200cاکبر', 'نجات', 'زاره', 'احسان', 'غزال', 'طلحه', 'عبدالحسین', 'ماشاءالله', 'حمیرا', 'بنیامین', 'مکرمه', 'نسرین', 'کامله', 'صمصام', 'بلور', 'مجدالدین', 'راستین', 'هرون', 'سامیه', 'ارشاد', 'آران', 'شمیم', 'فرشته', 'امیر\u200cحسین', 'عبدالباسط', 'شکوفه', 'رایان', 'امیرمحسن', 'پیام', 'ایلماز', 'سچاد', 'سپیده', 'مالک', 'صهبا', 'شفیعه', 'طاهره', 'رایکا', 'سیدفرشاد', 'رأفت', 'ثاقب', 'سحر', 'حميد', 'پوریا', 'عسل', 'تمنا', 'محمدقاسم', 'صفیه', 'جاسم', 'عمران', 'مهناز', 'آتنا', 'هادى', 'مهتاب', 'شاهین', 'محمود', 'سمیع', 'متین', 'اکرم', 'راحله', 'ابولفضل', 'مرجع', 'وحید', 'سها', 'صاعد', 'روژان', 'مشهود', 'عینعلی', 'آرام', 'نسترن', 'نسیم', 'حسام', 'سیدرضا', 'ضرغام', 'میحاد', 'کیان', 'هژیر', 'اميرعلي', 'مهراد', 'ملوک', 'علی\u200cاصغر', 'عادیات', 'شادن', 'عبدالخالق', 'مشکوه', 'صغری', 'هامر', 'مائده', 'ماهان', 'هلما', 'تیتکا', 'هایده', 'حامت', 'عبدالغفار', 'یوسف', 'پریسا', 'پریا', 'سامی', 'امینه', 'مسلم', 'نسيم', 'گلنار', 'ندا', 'مرسده', 'مژگان', 'مانی', 'ریحان', 'الاهه', 'فصیحه', 'تکتم', 'واحد', 'سار', 'اسنا', 'پژمان', 'اهدا', 'پرهام', 'عامر', 'سامر', 'احمدعلی', 'مجتبى', 'کیارش', 'آرزو', 'هاجر', 'عطا', 'راحیل', 'سامیرا', 'محنا', 'امیرمهران', 'نجوا', 'پيام', 'پويان', 'یسری', 'مینو', 'عبادالله', 'غضنفر', 'مینا', 'عبدالجواد', 'حمیدرضا', 'سیف\u200cالله', 'دیوا', 'نقی', 'صفر', 'عاشیه', 'یک', 'فریبا', 'ثمینه', 'شبنم', 'سامره', 'افضل', 'فواد', 'آذر', 'سیدحمزه', 'سیدرسول', 'شهره', 'نظام', 'سمانه', 'بشری', 'شادمهر', 'هانيه', 'عمر', 'معصومه', 'احد', 'محمدرضا', 'مجیبه', 'رافق', 'مسیح', 'سیدعلیرضا', 'حدیث', 'جابر', 'علی', 'لادن', 'شریف', 'عمین', 'مجيد', 'علیم', 'یکتا', 'ساعد', 'امیرحسین', 'ساناز', 'نعمت', 'ورشان', 'منذر', 'صالح', 'اعلی', 'ام\u200cالبنین', 'یمنا', 'قدرت', 'ماهد', 'عبدالعظیم', 'فتانه', 'صباح', 'اشكان', 'محمدجواد', 'انسیه', 'فوزیه', 'پریسادایی', 'دارا', 'مهدیه', 'ابوالفضل', 'اسدالله', 'حنا', 'امیرعلی', 'فهیمه', 'فاطمه\u200cگرامی', 'هومن', 'مهدي', 'سعیده', 'گروه', 'ملیحه', 'ماتریکس', 'سونیا', 'کامبیز', 'صفی\u200cالدین', 'رضا', 'امیر\u200cمحمد', 'بهادر', 'حره', 'فتح\u200cالله', 'فریده', 'پدرام', 'عماد', 'مهلا', 'مصطفي', 'ارشیا', 'جلال', 'بهناز', 'کلثوم', 'امير', 'خیرالدین', 'آرش', 'سالار', 'مونا', 'ثریا', 'امیر\u200cعباس', 'شهاب', 'ساقی', 'فرج\u200cالله', 'حمید', 'آیت', 'محدثه', 'مهشاد', 'رامیار', 'پیروز', 'آصفه', 'فاخته', 'ناریه', 'ابوالحسن', 'سلیمه', 'جمیله', 'رگداد', 'لقمان', 'دنیا', 'تمیم', 'آزیتا', 'ارسلان', 'پارمیس', 'طهورا', 'کامیاب', 'رضوانه', 'نورالله', 'عظیمه', 'قیصر', 'عبدالجلیل', 'دانشجوی', 'ضیغم', 'لیالی', 'احترام', 'رژان', 'رسام', 'ذبیح\u200cالله', 'سلطان', 'ظهیره', 'شهلا', 'نوریه', 'آریان', 'مرضیه', 'نوید', 'عصمت', 'سوشا', 'عبدالرشید', 'ابراهیم', 'سیدامیرقاضی', 'مرضيه', 'منا', 'آرين', 'غزل', 'امیرعطا', 'غلامرضا', 'شکور', 'آیدا', 'هیمن', 'مرصاد', 'بلال', 'عبدالغنی', 'وثوق', 'طلوع', 'هانی', 'سعد\u200cالدین', 'باقر', 'ماجده', 'آلنوش', 'شمس', 'سید', 'جنت', 'کلیم', 'مظهر', 'پاتریس', 'زهره', 'ولید', 'محمدرسول', 'شعله', 'یمین', 'معراج', 'امیر\u200cمهدی', 'پرند', 'عنایت', 'غفار', 'سيّد', 'پاتریک', 'نغمه', 'امیرمحمد', 'لیلا', 'سیدسجاد', 'آرشام', 'آیلار', 'البرز', 'ضیا', 'صدر', 'مهران', 'بنيامين', 'نسا', 'شفیع', 'رقیه', 'رفیع', 'عبدالحلیم', 'حدیثه', 'ميلاد', 'شعیب', 'عیسی', 'عنایت\u200cالله', 'عبدالله', 'کیومرث', 'کیا', 'عبدالفتاح', 'عظیم', 'پرنیان', 'سکینه', 'تیم', 'بهروز', 'سایت', 'سالمه', 'غیاث\u200cالدین', 'فاتح', 'مازیار', 'خلیل', 'حجت', 'راشن', 'مژده', 'محراب', 'ادیب', 'ماهنامه', 'آنی', 'رجب', 'شاهر', 'امین', 'عبیدالله', 'هدی', 'مچید', 'بنفشه', 'منصوره', 'خسرو', 'شکرعلی', 'خیرعلی', 'رویا', 'مقداد', 'هیبت', 'رامین', 'عرفان', 'سیما', 'دانوش', 'محمدصالح', 'بهار', 'ناصر', 'بتول', 'احلام', 'حلما', 'ظهیر', 'عبدالجبار', 'عبدالوهاب', 'فریدون', 'فرشاد', 'عبدالحمید', 'صابرین', 'سمیر', 'عاشور', 'غلامعباس', 'رباب', 'غلام', 'یاسر', 'مرشد', 'میعاد', 'حامده', 'هود', 'سيدمرتضي', 'محسنه', 'الینا', 'سعيد', 'فائز', 'عبدالرحیم', 'فاطیما', 'شهریار', 'ارمغان', 'عارفه', 'شقایق', 'عباد', 'گلستان', 'مهرناز', 'مهیره', 'کیمیا', 'عادله', 'عبدالکریم', 'جاهد', 'ملیکه', 'کامران', 'رجا', 'عبدالنبی', 'صفی', 'شريف', 'رزیتا', 'عبدالقاهر', 'جواهر', 'شیما', 'نام', 'ماریه', 'صابره', 'امیرمهدی', 'حسنا', 'سلاله', 'امیر\u200cطاها', 'رمضان', 'اقدس', 'مجتبی(شاهپور)', 'سلمان', 'صفار', 'ثنا', 'ملینا', 'نعیم', 'سعود', 'داود', 'حکیمه', 'صابر', 'مصیب', 'فتحعلی', 'لمیا', 'صیام', 'شجاع\u200cالدین', 'لیث', 'کوثر', 'مجتبی', 'عبدالعلی', 'ضرغامه', 'عامره', 'هدیه', 'مجید', 'اسامه', 'عبداله', 'شهیر', 'محتشم', 'یونس', 'محبوب', 'سیدمحمدمسعود', 'حوا', 'جلیل', 'محمدحسن', 'نسیبه', 'رمیصا', 'سیدامیرحسین', 'ماجد', 'همت', 'کاشف', 'حانیه', 'فائقه', 'مکیه', 'زاکیه', 'آرمان', 'نعیما', 'صدرالدین', 'ایدین', 'ليلا', 'بهرام', 'سیدعلی', 'یاسین', 'سحرمحمد', 'پویان', 'نصیر', 'المیرا', 'ماندانا', 'رانیا', 'ساهره', 'باران', 'شفیقه', 'فایضه', 'مهدی', 'بهنام', 'سپهر', 'اسداله', 'ظریف', 'جبار', 'رئوف', 'نسرين', 'انیس', 'قمر', 'خزعل', 'نادیه', 'عزیز', 'نادر', 'دریا', 'جواد', 'صمد', 'محمدسعید', 'فاطمه', 'وسیمه', 'نجف', 'آرمین', 'قدیسه', 'ذبیح', 'شیبان', 'قهار', 'طنین', 'عباسعلی', 'عبدالناصر', 'قائد', 'زینعلی', 'ژیار', 'تينا', 'آسیه', 'پري', 'مصطفی', 'مستر', 'آنيتا', 'مهپی', 'عبدالستار', 'لاوان', 'وجیهه', 'فریبرز', 'تسنیم', 'صحرا', 'کامیار', 'حلیه', 'سیاوش', 'داريوش', 'معید', 'نشاط', 'هانیه', 'نصیبه', 'منوره', 'موسی', 'زیبا', 'فراز', 'سیدامیرمحمد', 'افشین', 'میلاداسماعیل', 'سیدکریم', 'تقی', 'نجلا', 'شهروز', 'حبیب', 'پارسا', 'نازنين', 'سهيل', 'هانیا', 'طراوت', 'خیراالله', 'عفت', 'سمیح', 'صفی\u200cالله', 'منصور', 'نوال', 'نگین', 'مرىم', 'هادی', 'مشیر', 'سهیل', 'پیمان', 'عدنان', 'کامی', 'عبدالرزاق', 'نوشی', 'رو', 'الیاس', 'کیوان', 'بیتا', 'آیه', 'جعفر', 'اصغر', 'جادی', 'رافعه', 'مسعود', 'طلایه', 'راشد', 'حسنعلی', 'گلسا', 'سيده', 'افق', 'خضرا', 'اروشا', 'منیره', 'کوکب', 'رزاق', 'نهام', 'هاشم', 'علوان', 'دانيال', 'مراد', 'ارس', 'علیرضا', 'عفیفه', 'عزت', 'كيارش', 'زید', 'سمر', 'مارال', 'فرزان', '\u200cهانا', 'سپيده', 'طلا', 'فخرالدین', 'ولی', 'بهمن', 'شاهد', 'نعمان', 'شهرام', 'اسحاق', 'سیدمرتضا', 'نفیسه', 'واله', 'فرزین', 'شمیمه', 'هدایت', 'یگانه', 'مهدیس', 'فرساد', 'افسون', 'راشا', 'راحل', 'اطهر', 'ثمر', 'محیا', 'نصرالله', 'خدیجه', 'سیدمصطفی', 'محمدکاظم', 'غلامحسین', 'فرهاد', 'راضیه', 'شرکت', 'معین', 'آزاده', 'مبینا', 'سدن', 'ساجد', 'عزت\u200cالله', 'حنّان', 'کاظم', 'طیب', 'سومینا', 'سبا', 'زهیر', 'جلوه', 'لطفعلی', 'حداد', 'وصال', 'صلاح', 'عالمه', 'ظفر', 'سایه', 'صائب', 'عبدالمحمد', 'فاضل', 'جعفرامامی', 'شایگان', 'سیامک', 'بصیر', 'محمداعظم', 'معبود', 'عبدالباقی', 'عبدالرحمان', 'فرزانه', 'فرید', 'بهلول', 'عبدالرضا', 'لؤی', 'آزيتا', 'تراب', 'بها', 'الهه', 'آفاق', 'زمزم', 'صدیق', 'بهراد', 'قاسم', 'سیداشکان', 'علاء\u200cالدین', 'عذرا', 'الهام', 'مهسا', 'سیدامیر', 'حدیقه', 'شریفه', 'وسیم', 'ذوالفقار', 'فرنام', 'ادریس', 'آتیه', 'کریم', 'ایناس', 'سيد', 'پریدخت', 'نوین', 'ناهید', 'سارا', 'سما', 'اعتبار\u200cعلی', 'داریوش', 'ایمان', 'طلیعه', 'ساینا', 'سعيده', 'مهرداد', 'فائزه', 'آمنه', 'حفصه', 'صدیقه', 'ساغر', 'مرصع', 'لیلیا', 'محمدمهدی', 'حسین', 'سعدی', 'عابد', 'لیلی', 'واجد', 'علي', 'فریدالدین', 'وحدت', 'مهیار', 'ضحی', 'ندیمه', 'ﻣﻬﺪﻱ', 'داوود', 'قنبر', 'عبدالملک', 'سیدحسن', 'روح\u200cالله', 'رحیم', 'عارف', 'زینت', 'خالد', 'احمدرضا', 'زعیم', 'عین\u200cالله', 'منوچهر', 'حیات', 'عزیزه', 'فرهود', 'هنیا','هستی']
    politicsURL = {
        'irna': 'https://www.irna.ir/rss/tp/5',}
    economyURL = {
        'irna': 'https://www.irna.ir/rss/tp/20',}
    worldURL = {
        'irna': 'https://www.irna.ir/rss/tp/1',}
    socialURL = {
        'irna': 'https://www.irna.ir/rss/tp/32',}
    sportsURL = {
        'irna': 'https://www.irna.ir/rss/tp/14',}
    scienceURL = {
        'isna': 'https://www.isna.ir/rss/tp/5',}
    cultureURL = {
        'irna': 'https://www.irna.ir/rss/tp/41',}
    TimeMustWakeUp=[-1,-1]
    return [
                [['چطوره',"احوالت","حالت","چطوری","خوبی","حالت خوبه","حالت خوب است"],["عالی","خوبم","بهتر از این نمیشه","یِکَم خستم","بهترینم"],[]],
                [["اسمت"],["من اکبر هستم"],[]],
                [["کی هستی"],[" من اکبر هستم.  یک ربات با هوشِ مصنوعیِ قوی و آماده خدمتِ به شما"],[]],
                [["چی کار","چیکار"],["من هر کاری که نیاز داشته باشی رُ میتونم انجام بدم"],[]],
                [["ساخته","ساختن"],["آقایان علیرضا شعبانی و پارسا سلیمانی"],[]],
                [["درود بر شما","درود","سلام","سلامٌ عَلِیکُم","درود فراوان","سلام بر تو باد","درودِ فراوان","سلام"],["درود بر شما","درود","سلام","سلامٌ عَلِیکُم","درود فراوان","سلام بر تو باد","درودِ فراوان"],[]],
                [["سوره","قران","قرآن"],[],[[MusicPlay,(random.choice(["Sooreh_1"]))+"()"+text]]],
                [["اذان","ازان"],[],[[MusicPlay,((random.choice(["Azan"]))+"()"+text)]]],
                [["بهنام","بانی"],[],[[MusicPlay,random.choice(MusicNames("‌BehnamBani",1))+"()"+text]]],
                [["حامد","بهرام"],[],[[MusicPlay,random.choice(MusicNames("HamedBahram",1))+"()"+text]]],
                [["آرون","افشار"],[],[[MusicPlay,random.choice(MusicNames("AronAfshar",1))+"()"+text]]],
                [["موزیک ترکیه","آهنگ ترکیه",],[],[[MusicPlay,random.choice(MusicNames("Turkish",1))+"()"+text]]],
                [["گیتار","جیپسی","فلامینگو"],[],[[MusicPlay,random.choice(MusicNames("Gypsy",1))+"()"+text]]],
                [["جهان بخش","جهانبخش","بابک"],[],[[MusicPlay,random.choice(MusicNames("BabakJahanbakhsh",1))+"()"+text]]],
                [["موزیک","آهنگ","اهنگ"],[],[[MusicPlay,(random.choice(AllMusicsList())+"()"+text)]]],     #all musics
                [["پسری","پسر هستی","دختری","دختر هستی","جنسیت"],["من یک ربات هستم ولی اسمِ من پسرانه است"],[]],
                [["چند سال","به دنیا","تولد","سن"],["من کمتر از یک سال دارم"],[]],
                [["عشقم","عزیزم","خوشم میاد","عاشقتم","دوستت دارم","دوست دارم"],["من هم شما رو دوست دارم"],[]],
                [["چه کاری علاقه داری","چه کاری لذت میبری","چه کاری خوشت میاد","چه کاری رو دوست داری","چه کاری را دوست داری","چه کاری دوست داری"],["من عاشقِ باطری هستم و همیشه دوست دارم باطری اِستِعمال کنم"],[]],
                [["رنگ","رنگی"],["من عاشق رنگِ سفید هستم"],[]],
                [["چند شنبه"],[],[[Day]]],
                [["چندم","تاریخ"],[],[[Date]]],
                [["ساعت چنده"],[],[[Time_Now]]],
                [["خبر فرهگ","اخبار فرهگ","خبر هنر","اخبار هنر"],[],[[News,cultureURL]]],
                [["خبر علم","اخبار علمی","خبر دانش","اخبار دانش"],[],[[News,scienceURL]]],
                [["خبر ورزش","اخبار ورزشی"],[],[[News,sportsURL]]],
                [["خبر اجتماع","اخبار اجتماع"],[],[[News,socialURL]]],
                [["خبر جهان","اخبار جهان"],[],[[News,worldURL]]],
                [["خبر اقتصاد","اخبار اقتصاد"],[],[[News,economyURL]]],
                [["خبر سیاس","اخبار سیاس"],[],[[News,politicsURL]]],
                [["اخبار"],[],[[News,random.choice([sportsURL,socialURL,worldURL,economyURL,politicsURL,cultureURL,scienceURL])]]],
                [["طلا"],[],[[GoldPrice,PricesInfo]]],
                [["ربع سکه"],[],[[RobCoin,PricesInfo]]],
                [["نیم سکه"],[],[[HalfCoinPrice,PricesInfo]]],
                [["تمام سکه","سکه تمام"],[],[[FullCoinPrice,PricesInfo]]],
                [["دلار"],[],[[DollarPrice,PricesInfo]]],
                [["یورو"],[],[[EuroPrice,PricesInfo]]],
                [["پوند"],[],[[PondPrice,PricesInfo]]],
                [["درهم"],[],[[DerhamPrice,PricesInfo]]],
                [["لیر"],[],[[LirPrice,PricesInfo]]],
                [["بیتکوین","بیت کوین"],[],[[BitCoinPrice,PricesInfo]]],
                [["جواب","مجموع","حاصل"],[],[[Calculater,text]]],
                [["هوا","دما","باد"],[],[[Temperature,text]]],
                [["جک","جوک"],[],[[Joke]]],
                [["معکوس","بر عکس"],[],[[Joke]]],
                #reverse_True_and_False
                #calculating_game()
                [["سرچ","جست و جو","جستجو"],[],[[Search,str(text)]]],
                [["پادکست"],[],[[MusicPlay,(random.choice(["Podcast"]))+"()"+text]]],
                [["شعر","اخوان","دکلمه","باغ بی برگی"],[],[[MusicPlay,(random.choice(["BaghBiBargi"]))+"()"+text]]],
                [["سرود"],[],[[Anthems,text]]],
                [["دارو اضافه"],[],[[AddToReminder]]],
                [["دارو حذف"],[],[[DeleteFromReminder]]],
                ]
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
def Is_numeric(Text):
    if Text.isnumeric()==True:
        return True
    elif Text[0]=="-":
        TEXT=Text.replace("-","")
        return TEXT.isnumeric()
    else:
        return False
def calculating_game():
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

def Anthems(text="nothing"):
    list_en=["Poland","Russia","Soviet","United Kingdom","Brazil","Canada","France","Germany","Iran","Italy"]
    list_fa=[["لهستان"],["روسیه"],["شوروی"],["اینگیلیس","انگلیس","انگلستان","بریتانیا"],["برزیل"],["کانادا"],["فرانسه"],["آلمان","المان"],["ایران"],["ایتالیا"]]
    for Box in list_fa:
        for Little_Box in Box:

            if Little_Box in text:
                MusicPlay(list_en[list_fa.index(Box)]+"()"+text)
                return 
    
    TTS(random.choice(["پیدا نکردم","تو انبار نداریم"]),"fa")

"""
 ██████╗  ███████╗ ██╗   ██╗ ██╗ ███████╗ ████████╗  ██████╗  
 ██╔══██╗ ██╔════╝ ██║   ██║ ██║ ██╔════╝ ╚══██╔══╝ ██╔═══██╗ 
 ██████╔╝ █████╗   ██║   ██║ ██║ ███████╗    ██║    ██║   ██║ 
 ██╔══██╗ ██╔══╝   ╚██╗ ██╔╝ ██║ ╚════██║    ██║    ██║   ██║ 
 ██║  ██║ ███████╗  ╚████╔╝  ██║ ███████║    ██║    ╚██████╔╝ 
 ╚═╝  ╚═╝ ╚══════╝   ╚═══╝   ╚═╝ ╚══════╝    ╚═╝     ╚═════╝ 
"""