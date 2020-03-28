


#in the name of who made humans.....
import speech_recognition as sr
import random
import wikipedia
from googletrans import Translator
import os
from playsound import playsound
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
def DATA_function(text,PricesInfo):
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
    return [#[["راه","جلو"],["انجام شد","حتما","الان","درحال انجام"],[[Walk]]],
                #[["دست راست"],["انجام شد","حتما","الان","درحال انجام"],[[RightHand]]],
                #[["دست چپ"],["انجام شد","حتما","الان","درحال انجام"],[[LeftHand]]],
                #[["پرواز"],["انجام شد","حتما","الان","درحال انجام"],[[Fly]]],
                #[["رقص"],["انجام شد","حتما","الان","درحال انجام"],[[Dance]]],
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
                #[["بشین"],["انجام شد","حتما","الان","درحال انجام"],[[SitDown]]],
                #[["پاشو"],["انجام شد","حتما","الان","درحال انجام"],[[StandUp]]],
                #[["بخند"],["انجام شد","حتما","الان","درحال انجام"],[[Laugh]]],
                #[["گریه"],["انجام شد","حتما","الان","درحال انجام"],[[Cry]]],
                #[["تعجب"],["انجام شد","حتما","الان","درحال انجام"],[[Wtf]]],
                #[["درد"],["انجام شد","حتما","الان","درحال انجام"],[[Pain]]]
                [["سرچ","جست و جو","جستجو"],[],[[Search,str(text)]]],
                [["پادکست"],[],[[MusicPlay,(random.choice(["Podcast"]))+"()"+text]]],
                [["شعر","اخوان","دکلمه","باغ بی برگی"],[],[[MusicPlay,(random.choice(["BaghBiBargi"]))+"()"+text]]]
                #[["ساعت"],[],[[TimeNow]]]
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
PricesInfo=GetSomeInfoAboutPrice()
TTS("در خدمتم ","fa")

while True:
  
    if True:
        MusicPlay("Click"+"()"+"0.0")
        audio = GetVoice()
        #text = input()
        MusicPlay("WaitAna"+"()"+"0.0")
        text= AnalyseVoice(audio)
        if text!="" and "خاموش" not in text:
            print (text)
            Analyse(text,DATA_function(text,PricesInfo))  
        else:
            TTS("خاموش" , "fa")
            while "روشن" not in text:
                MusicPlay("Click")
                audio = GetVoice()
                text= AnalyseVoice(audio)

 
