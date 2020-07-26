from  Lib.___Libraries___ import *
#from  DATA import *

#-_-_-_-l I B R A R I E S-_-_-_-#-_-_-_-
# ¯\_(ツ)_/¯

class Audio():
    def MusicPlay(self,MusicName,text="Full"):
        print (MusicName,text)
        #Others().BlockPrint()
        player = MPyg321Player()       # instanciate the player
        Pwd=(str(Data().PWD())+"/")
        print ("*/*-+*/*-+/*-*8/*->>"+ " "+ Pwd)
        Locations=[""]+Data().FindFolders(Pwd+"/Audios")
        Pwd+="Audios/"
        print (Locations)
        for Loc in Locations:
            Path=Pwd+Loc+"/"+MusicName+".mp3"
            
            if os.path.exists(Path):
                print (Path)
                player.play_song(Path)
                break

        time.sleep(Audio().FindHowMuchToPlay(Path,text)) 
        #time.sleep(Audio().FindHowMuchToPlay(MusicName+".mp3",text)) 
        try:
            if int(text)!=0:              
                player.quit()  
        except:
            None
        Others().EnablePrint()
            
    def LenMusic(self,MusicNameWithDotMp3):
        audio = MP3(MusicNameWithDotMp3)
        return audio.info.length
    
    def FindHowMuchToPlay(self,MusicNameWithDotMp3,text):
        text=text.split(" ")
        Second=""
        for i in range (len(text)):
            try:
                text[i]=int(text[i])
                Second=int(text[i])
            except:
                None
        if Second=="":
            return Audio().LenMusic(MusicNameWithDotMp3)
        else:
            return Second
    
    def Anthems(self,text="nothing"):
        list_en=["Poland","Russia","Soviet","United Kingdom","Brazil","Canada","France","Germany","Iran","Italy"]
        list_fa=[["لهستان"],["روسیه"],["شوروی"],["اینگیلیس","انگلیس","انگلستان","بریتانیا"],["برزیل"],["کانادا"],["فرانسه"],["آلمان","المان"],["ایران"],["ایتالیا"]]
        for Box in list_fa:
            for Little_Box in Box:

                if Little_Box in text:
                    Audio().MusicPlay(list_en[list_fa.index(Box)],text)
                    return 
        
        Audio().TTS(random.choice(["پیدا نکردم","تو انبار نداریم"]),"fa")
    
    def CompleteVoiceAnalyse(self):
        try:
            Audio().MusicPlay("Click","0")
            audio = Audio().GetVoice()
            Audio().MusicPlay("hmmm+WaitAna","0")
            text = Audio().AnalyseVoice(audio)
            
        except:
            text=""
        return text
    
    def GetVoice(self):    
        mic = sr.Microphone()
        r=sr.Recognizer()
        with mic as source:
            audio = r.listen(source)
        return (audio)   
    
    def AnalyseVoice(self,audio):
        r=sr.Recognizer()
        text = r.recognize_google(audio, language='fa-IR')# language  set farsi :)
        return text
    
    def MusicNames(self,name,num):
        List=[]
        for i in range (int(num)):
            List.append(str(name)+"_"+str(i+1))
        return List
    
    def AllMusicsList(self):
        List=[Audio().MusicNames("BehnamBani",1)+Audio().MusicNames("HamedBahram",1)+Audio().MusicNames("AronAfshar",1)+Audio().MusicNames("Turkish",1)+Audio().MusicNames("Gypsy",1)+Audio().MusicNames("BabakJahanbakhsh",1)]
        return List[0]
    
    def TTS_Offline(self,text,language):
        os.system("espeak -v "+'"'+str(language)+'"'+" "+'"'+str(text)+'"'+" "+"-s 20 -g 2")
    
    def TTS(self,TEXT,fa="Nothing"):
        doc = requests.get("http://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=C6QAXK7BNFEI10M&Text="+TEXT+"&Speaker=Male1&Format=mp3&GainLevel=5&PitchLevel=4&PunctuationLevel=0&SpeechSpeedLevel=5&ToneLevel=0&Quality=low&BeginningSilence=0&EndingSilence=0&Base64Encode=0")
        #with open(Data().PWD()+"/Audios/Talks/"+'Talk.mp3', 'wb') as f:
        with open('Audios/Talks/Talk.mp3', 'wb') as f:
            f.write(doc.content)
        Audio().MusicPlay("Talk")
    
    def CompleteVoiceAnalysMute(self):
        try:
            audio = GetVoice()
            text = AnalyseVoice(audio)
        except:
            text=""
        return text

    
    def IDK(self):
        Audio().TTS(random.choice(["متاسفانه متوجهِ منظورتون نِمیشم","متاسفانه متوجه نَشدم","شرمنده متوجه منظورتون نِمیشم","شرمنده متوجهِ نشدم","من دارم یاد میگیرم و متوجهِ منظورتون نِمیشم","متاسفانه نفهمیدم"]),"fa")      


class Data():
    def Search(self,text):
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
        Audio().TTS(a,"fa") 

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
    
    def DATA_function(self,text):
        return DATA_intents(text)
    
    def Analyse_Function(self,text,DATA):
        Rank=[]
        for Box in DATA["DATA_intents"]:
            NotQualify=False
            Similarity_Keywords=0
            FirstLayerScore=0
            SecoundLayerScore=0
            for MustBekeyword in Box["MustBeKeywords"]:
                if type(MustBekeyword)==list:
                    Same=0
                    for MustBekeywordInList in MustBekeyword:

                        if MustBekeywordInList in text:
                            Same+=1

                    if Same==0:
                        NotQualify=True
                else:
                    if MustBekeyword not in text:
                        NotQualify=True
            if NotQualify==False:
                for FirstLayerKeyword in Box["FirstLayerKeywords"]:
                    if FirstLayerKeyword in text:
                        FirstLayerScore+=1
                        print (FirstLayerKeyword)
                if FirstLayerScore!=0:
                    for SecoundLayerKeyword in Box["SecoundLayerKeywords"]:
                        if SecoundLayerKeyword in text:
                            SecoundLayerScore+=1
                Similarity_Keywords=FirstLayerScore+SecoundLayerScore
            Rank.append([Similarity_Keywords, DATA["DATA_intents"].index(Box)])
            
        BestMatch=(max(Rank))
        if BestMatch[0]==0:
            return False
        
        print ("Same Keywords : ",BestMatch[0])
        print ("the Tag : ",DATA["DATA_intents"][BestMatch[1]]["Tag"])
        #print ("KeyWords : ",DATA["DATA_intents"][BestMatch[1]]["KeyWords"])
        print ("Answers : ",DATA["DATA_intents"][BestMatch[1]]["Answers"])

        if DATA["DATA_intents"][BestMatch[1]]["Answers"] != []:
            Audio().TTS(random.choice(DATA["DATA_intents"][BestMatch[1]]["Answers"]))
            
        if DATA["DATA_intents"][BestMatch[1]]["Actions"] != []:
            for Box in DATA["DATA_intents"][BestMatch[1]]["Actions"]:
                Box[0](*Box[1:len(Box)])

        return True
    
    def WHQ(self,text):
        WHlist=['کیه','کدامه','چطوره','چرا' ,'چرا','چه','چطور','چه','کجا','کی','چی','کدام',"چگونه"]
        for WH in WHlist:
            for word in (text.split(" ")):
                if word==WH:
                    return True
        return False
    
    def YNQ(self,text):
        YNlist=['آیا',"ایا"]
        for YN in YNlist:
            if YN in text:
                return True
        return False
    
    def MergeList(self,List):
        Out=""
        for word in List:
            if word == "تو" or word == "شما":
                word="من"
            Out+=word+" "
        Out=Out.replace("شما","من")
        Out=Out.replace("تو","من")
        return Out
    
    def Analyse_Closest(self,text,DataBase):
        DataTouple=DataBase
        DataList=[]
        TextSplit=text.split(" ")
        for List in DataTouple:
            RemoveList=list(List)
            Similarity=0
            for ClientWord in TextSplit:
                for DataWord in List:
                    if ClientWord==DataWord:
                        RemoveList.remove(DataWord)
                        Similarity+=1
                        break 
            try:
                Randeman=Similarity/len(List)
            except:
                Randeman=0
            DataList.append([Randeman,DataTouple.index(List),Data().MergeList(RemoveList)])
        #print (max(DataList))
        BestChoice=max(DataList)
        print ( "In DataBase:  " , BestChoice)
        """if float(BestChoice[0])<=0.55:
            return False"""
        
        print (BestChoice[2])
        Audio().TTS(BestChoice[2])
        return True
    
    def AddToDataBase(self,text):
        FileData=open("___DataBase___.py","a+")
        List=text.split(" ")
        print (","+str(List)+"\n")
        FileData.write(str(","+str(List)))
        FileData.close()

    def PWD(self):
        import subprocess
        proc = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out=str(out)
        out=(out[2:len(out)-3])
        return out

    def FindFolders(self,path):
        mypath=path
        Files_Raw = [f for f in os.listdir(mypath)]
        #print (Files_Raw)
        Folders=[]
        Files=[]
        for File in Files_Raw:
            if len(File.split("."))==1:
                Folders.append(File)
            else:
                Files.append(File)
        return Folders

    def FindFiles(self,path):
        mypath=path
        Files_Raw = [f for f in os.listdir(mypath)]
        #print (Files_Raw)
        Folders=[]
        Files=[]
        for File in Files_Raw:
            if len(File.split("."))==1:
                Folders.append(File)
            else:
                Files.append(File)       
        return Files


class DateAndWeather():
    def Date(self):
        Months=["فَروَردین","اَردیبِهِشت","خُرداد","تیر","مُرداد","شَهریوَر","مِهر","آبان","آذَر","دِی","بَهمَن","اِسفَند"]
        Date=(JalaliDate.today())
        Date=str(Date).split("-")
        if str(Date[2])[0]=="0":
            Date[2]=Date[2][1]
        Audio().TTS("روزِ"+str(Date[2])+"اُمِ"+","+"ماهِ"+Months[(int(Date[1])-1)]+","+"سالِ"+str(Date[0]), "fa")
    
    def Time_Now(self):
        time=(khayyam.JalaliDatetime.now().strftime('%C')).split(" ")
        time=(time[-2])
        time=time.split(":")
        for i in range (len(time)):
            time[i]=int(time[i])
            time[i]=str(time[i])
        Audio().TTS("ساعت"+time[0]+","+"ُّ"+","+time[1]+"دقیقِ"+"ُ"+","+time[2]+"ثانیه","fa")
    
    def Day(self):
        time=(khayyam.JalaliDatetime.now().strftime('%C')).split(" ")
        day=time[-6]
        try:
            day=time[-7]+" "+day
        except:
            None
        Audio().TTS(day,"fa")
    
    def Temperature(self,text):
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
                    Audio().TTS("امروز","fa")
                if day==3:
                    Audio().TTS("فردا","fa")
                if day==4:
                    Audio().TTS("پس فردا","fa")
                if day==5:
                    Audio().TTS("سه روز بعد","fa")
                if day==6:
                    Audio().TTS("چهار روز بعد","fa")

                val = daily.get(day)
                print (val)
                if "خلاصه" in text:
                    Sum=(Others().Translate((val['summary']),"fa"))
                    try:
                        if "نور" in Sum:
                            Sum=Sum.replace("نور","سبک")
                        TTS (Sum,"fa")
                    except:
                        None
                    
                if "دما" in text or "هوا" in text:
                    Audio().TTS (("کمترین دما"+str(int(val['temperatureMin'] ))+"درجه سانتی گِراد"),"fa")
                    Audio().TTS (("بیشترین دما"+str(int(val['temperatureMax']))+"درجه سانتی گِراد"),"fa")
                if "سرعت" in text:
                    Audio().TTS ((" سرعتِ باد"+str(int(val['windSpeed']))+"کیلومتر بر ساعت"),"fa")
                if "امروز" in text:
                    break
                if "پس فردا" in text and day==3:
                    break


class Game():
   
    def Game_Name(self,List):
        Audio().MusicPlay("Click","0")
        Input=Audio().GetVoice()
        Audio().MusicPlay("WaitAna","0")
        Input=Audio().AnalyseVoice(Input)
        if Input in List:
            List.remove(Input)
        else:
            Audio().TTS("دوباره امتحان کن , یک اسم بگو","fa")
            Audio().MusicPlay("Click","0.0")
            Input=Audio().GetVoice()
            Audio().MusicPlay("WaitAna","0")
            Input=Audio().AnalyseVoice(Input)
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
            Audio().TTS (MyName,"fa")
            Audio().MusicPlay("Click","0")
            Input=Audio().GetVoice()
            Audio().MusicPlay("WaitAna","0")
            Input=Audio().AnalyseVoice(Input)
            if Input in List and Input[0]==MyName[len(MyName)-1]:
                List.remove(Input)
            else:
                Audio().TTS("دوباره تلاش کن","fa")
                Audio().TTS(MyName,"fa")
                Audio().MusicPlay("Click","0")
                Input=Audio().GetVoice()
                Audio().MusicPlay("WaitAna","0")
                Input=Audio().AnalyseVoice(Input)
                if Input in List and Input[0]==MyName[len(MyName)-1]:
                    List.remove(Input)
                else:
                    Audio().TTS("شما باختی","fa")
                    return
    
    def calculating_game(self):
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
            Audio().TTS("شروع","fa")
            Audio().TTS(Text,"fa")
            Input=Audio().CompleteVoiceAnalyse()
            while Is_numeric(Input)==False:
                if Input=="تمام":
                    con=False
                    return 0
                else:
                    Audio().TTS("دوباره بگو")
                    Input=Audio().CompleteVoiceAnalyse()
            if Others().Calculater(Text)==int(Input):
                Audio().TTS("درسته","fa")
                level+=1
            else:
                Audio().TTS("غلطه","fa")
    
    def Reverse_True_and_False(self):
        list_questions=["آیا شما انسان هستید","یا بستنی داغ است","آیا زمین تخت است","آیا خورشید بنفش است","آیا جنگ خوب است","آیا فوتبال ورزش است","آیا قم کشور است","آیا فیل کوچک است","آیا ویروس بزرگ است","آیا رضا شاه وزیر بود","آیا شاهزاده وزیر است","آیا ماه ستاره است","آیا عراق شهر است","آیا پسر پدر وزیر پدرش است","آیا برج میلاد برج است","آیا شیر سیاه است","آیا سیاه روشن است","آیا خوبی بدی است","آیا اروپا کشور است","آیا بحرین بزرگ است","آیا آهن از پنبه سبک تر است"]
        key="nyyyynyyyyynyynyyyyyy"
        while True:
            Ind=random.randint(0,len(list_questions)-1)
            Audio().TTS(list_questions[Ind],"fa")
            iinput=Audio().CompleteVoiceAnalyse()
            if "بله" in iinput:
                if key[Ind]=="y":
                    Audio().TTS("درسته","fa")
                else:
                    Audio().TTS("غلطه","fa")
            elif "خیر" in iinput:
                if key[Ind]=="n":
                    Audio().TTS("درسته","fa")
                else:
                    Audio().TTS("غلطه","fa")
            else:
                Audio().TTS("باختی","fa")
                break
    
    def Find_Singer(self):
        #you should put the list of singers and their songs here
        #it should be a 2-D list and like the below sentence
        #[[song name.mp3,singer]]
        list_songs_and_singers=[[Audio().MusicNames("AronAfshar",1),"آرون افشار"],[Audio().MusicNames("HamedBahram",1),"حامد بهرام"],[Audio().MusicNames("‌BehnamBani",1),"بهنام بانی"]]
        while True:   
            list_artist=random.choice(list_songs_and_singers)
            Audio().MusicPlay(random.choice(list_artist[0])+"()20")
            Input=Audio().CompleteVoiceAnalyse()
            if list_artist[1] in Input:
                Audio().TTS("صحیح","fa")
            elif "بیرون" in Input:
                break
            else:
                Audio().TTS("اشتباه است")
                Audio().TTS(list_artist[1],"fa")
                return
    
    def Game_Panel(self,Class):

        NameAndFunctions=[[Class.Find_Singer,"حدس خواننده","خواننده"],[Class.Reverse_True_and_False,"بله و خیر معکوس","معکوس"],[Class.Game_Name,"بازی اسم ها","اسم"]]
        Audio().TTS("بازی مورد نظرتون رو بگید")
        text=input("SD")
        while Data().WHQ(text):
            Audio().TTS("بازی ها")
            for Game in NameAndFunctions:
                Audio().TTS(Game[1])
            text=Audio().CompleteVoiceAnalyse()
    
        for Box in NameAndFunctions:
            if Box[2] in text:
                Box[0]()
                break


class Others():
    def Calculater(self,text):
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
        Audio().TTS(l_full[0],"fa")
    
    def News(self,category):
        def parse_rss(rss_url):
            return feedparser.parse(rss_url)
        def get_headlines(rss_url):
            headlines = []
            feed = parse_rss(rss_url)
            for newsitem in feed['items']:
                headlines.append(newsitem['title'])

            return headlines
        allheadlines = []


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
            Audio().TTS(New,"fa")
    
    def Translate(self,text,translated_language):    #return translated text
        translator = Translator()
        result = translator.translate(str(text), dest=str(translated_language))
        translated=result.text
        Audio().TTS(translated)
    
    def Joke(self):
        jokes=['  دیدی درد نداشت؟        جمله نوستالژیک پدر و مادرها بعد آمپول زدن به بچه هاشون در حالی که بچه داره خون گریه میکنه     یعنی اون همه اشک ماله شوق بوده.', ' کار بابام از کولر گذشته       دیگه شبا بلند میشه میاد مودم رو خاموش میکنه!.', ' دکمه روشن کنترلو 20 بار می زنی تلویزیون روشن نمی شه     عصبانی می شی، 2 بار پشت سر هم محکم فشار می دی روشن می شه دوباره خاموش می شه!', ' دیگه به درجه ای از عرفان رسیدم که واسه خودم یه چیزی تعریف می کنم می خندم   تازه آخرش هم از خودم می پرسم جان من؟!', ' یکی از محاسبه هایی که سریع انجام می دیم، محاسبه فاصله من و دادشم و خاهرم نسبت به آیفونه وقتی یکی زنگ درو می زنه!', ' روزگارا که چنین سخت به من می گیری با خبر باش که خیلی داری سخت می گیری دیگه! مسخرشو درآوردی', ' از جلوی یه رستوران رد میشدم دیدم روی درش نوشته: لورل بیا هاردی برو!', ' امروز دست خط خودمو بردم دارو خونه …        بهم دارو داد !', ' یارو ميره تو صف نونوايي، شاطر نونوائی ميگه: نون تا اينجا بيشتر نميرسه، بقيه برن. ميگه: ببخشيد اگه ميشه جمعتر وايسين نون به ما هم برسه', ' اگه میشد دانشمندا یه وسیله اختراع میکردند که از خروپوف برق تولید کنه الان بابام یه نیروگاه هسته ای محسوب می شد !.', ' تا حالا دقت کردین کسایی که خروپف میکنن ،  زودتر خوابشون میبره !؟', ' رفتم دادگستری یارو میپرسه شکایت داشتید؟ گفتم پـَـــ نــه پـَـــ یه خورده برنج آوردم با ترازوی عدالت وزن کنم !.', '  رفتم باغ وحش از نگهبانه میپرسم ببخشید آقا قفس شیرا کجاست ؟ میگه بازدید کننده ای پـَـــ نــه پـَـــ نه از اقوامشون هستم اینورا کاری داشتم گفتم سری بهشون بزنم', '  اومدم در یخچالو باز میکنم دنبال غذا مامانم میگه گشنته؟ پـَـــ نــه پـَـــ اومدم ببینم کی هی چراغ این تو رو خاموش روشن می کنه!.', ' یه بیماری هست اسم نداره اما نتیجه ش     نگهداشتن شیشه عطرها و اسپری های تموم شده ست !.', ' ﺑﻪ ﺑﻌﻀﯽ ﻫﺎ ﺑﺎﻳﺪ ﺑﮕﯽ :  ﺍﮔﻪ ﻭﺍﺳﻪ ﻫﻤﻪ ﻗﺎﻃﯽ ﭘﺎﺗﯽ ﻣﻴﮑﻨﯽ ، ﻭﺍﺳﻪ ﻣﺎ ﻫﻨﻮﺯ ﺗﺎﺗﯽ ﺗﺎﺗﯽ ﻣﻴﮑﻨﯽ !.', ' بدترین چیز اون خنده ی اجباری برای حفظ آبرو بعد از یه زمین خوردن وحشتناکه', ' بعضیا واسه همــه اقیانوس آرام هستن اما تا به ما میرسن میشن تنگهء هرمز!', ' فکر کنم رمز موفقیتمو ۳ بار اشتباه زدم قفل شده ', ' یه وقتایی لازمــه از گوشیمون بشنویم “مشترک مورد نظر آدم نمیباشد … لـــطفا قطع کنید”!', ' امسال نمایشگاه کتاب نرفتم ، خودم تو خونه سیب زمینی سرخ کردم خوردم !', ' زندگی مثل شطرنج میمونه ، البته تو که بچه ای برو منج بازی کن !', ' باهمه وجودم سرمو روشونه مهربون تو میذارم و یواشکی دماغمو با لباست پاک میکنم!!', ' خیلی دلم برات تنگ شده…اونقدر که از دوریت گریه ام میگره… اما وقتی قیافت یادم میاد خندم میگیره!!', ' افتخار نکن که به اندازه تار موهات رفیق داری. وقتی محتاجشون میشی می فهمی که کچلی.', ' وقتی مو تو غذا باشه،فرقی نداره مژه ی دلبر باشه یا سیبیل اصغر آقا!', ' این دهه ۶٠یا که هی نسل سوخته نسل سوخته میکنن   فکر نکنن ما یادمون رفته ماه رمضوناشون تو زمستون بوده ..!', ' جمله ای که من هروقت یه آدم پولدار میبینم واسه آروم کردن خودم میگم: آرامشی که ما داریمو اونا ندارن!!', ' میدونم یکی هست که تو دلش وِلولـس واسه خواستنــم فقط نمیدونم کجاست؟', ' بچه که بودم فکر میکردم زمان قدیم همه جا سیاه سفید بوده', ' بابام ﻣﯿﮕﻪ ﺍﻭﻝﮔﻮﺵ ﮐﻦ ﺑﺒﯿﻦ ﭼﯽ ﻣﯿﮕﻢ     ﺑﻌﺪ ﯾﺎ ﻗﺒﻮﻝ ﮐﻦﯾﺎ ﺑﺮﻭ ﻓﮑﺮﺍﺗﻮ ﮐﻦ ﺑﻌﺪ ﻗﺒﻮﻝ ﮐﻦ !', ' اومدم خونه به مامانم میگم گشنمه، میگه عزیزم نون هس ،تخم مرغ هس، روغنم هس،  برو هر چى دوس دارى درست کن بخور!', ' دو ماهه دارم هر شش ساعت یه بار دوتا آنتی هیستامین میندازم تو جیبام    ولی بازم جیب ما به پول حساسیت داره!', ' یه وختایی نمیرم دمه یخچال که پیشه من شرمنده نشه... خدا هیچ یخچالی رو شرمنده صاحبش نکنه.', ' دیگه کار از کلیپس گذشته برخی از دخترا در حال ساخت مسکن مهر رو سرشون هستند…!', '  اگه قرار باشه اون دنیا تو بهشت موسیقی های خوب گوش کنیم، فک کنم تو جهنم تتلو پخش کنن ', ' من حتی اگه بمیرم مامانم میاد سر قبرم میگه ببین بچه ی فلانی نصف توعه ولی زنده است ', ' پارسال با بابام دعوام شد بهش گفتم بالاخره یه روز از این خونه میرم الان یک ساله هر روز موقع شام و نهار میگه به به, شما که هنوز نرفتی.', '  دوستان نگران نباشید ویروس کرونا زود خراب میشه میمیره چون جنسش چینیه ', '  انقدر که توی سایت ها ربات نبودنمو ثابت کردم توی زندگیم آدم بودنمو ثابت نکردم ', '  دلم برای روزایی که تو دبستان با بچه ها دعوامون میشد کیفشو برمیداشتم پرت کنم میگف ننننددداااازززقران توشه تنگ شده... ', ' هم عاشقتم , هم ازت متنفرم , میانگین که بگیری میبینی برام مهم نیستی !', ' به سلامتی پنگوئن که یه ذره قد داره، اما بازم لاتی راه میره ….', ' بزرگترین حرف های کینه توزانه با این جمله توجیه میشه : ” به خاطر خودت میگم “', ' یه شلغمم نشدیم یکی کوفتمون کنه خوب شه…..!!', ' یه کتابم نشدیم حداقل دوست مهربان بشیم !!', ' طنز بگو', ' حیف نون به باباش میگه : پنکه خراب شدهباباش میگه : خوب معلومه پنج نفری زیرش میخوابین ، میخوای خراب نشه ؟!!', ' ه حیف نون میگن این خیابون کجا میره ؟میگه من ۴۰ ساله تو این خیابون زندگی میکنم تا حالا ندیدم جایی بره !', ' احساسی که با خنده همراه است.']
        Audio().TTS(random.choice(jokes),"fa") 

    def BlockPrint(self):
        sys.stdout = open(os.devnull, 'w')

    def EnablePrint(self):
        sys.stdout = sys.__stdout__


class Prices():
    def GetSomeInfoAboutPrice(self):
        doc = requests.get('https://currency.jafari.pw/json')
        doc=doc.text
        text = json.loads(doc)
        Dic={}
        for i in text:
            for Box in text[i]:
                #print (Box)
                if "Name" in Box:
                    Dic[Box["Name"]]=Box["Rate"]
                if "Currency" in Box:
                    Dic[Box["Currency"]]=Box["Buy"]
                if "Coin" in Box:
                    Dic[Box["Coin"]]=Box["Buy"]
        return Dic
    
    def RobCoin(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت ربع سکهْ"+str(text["1/4 Azadi"])+"تومن")
    
    def HalfCoinPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت نیم سکهْ"+str(text["1/2 Azadi"])+"تومن")
    
    def FullCoinPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت سکه بهار آزادیْ"+str(text["1 Old Azadi"])+"تومن")
    
    def DollarPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        print (text)
        Audio().TTS("قیمت دُلارْ"+str(text["US Dollar"])+"تومن")
    
    def EuroPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت یُرُ"+str(text["Euro"])+"تومن")
    
    def PondPrice(self): 
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت پوند انگلیسْ"+str(text["British Pound"])+"تومن")
    
    def DerhamPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت دِرهمْ"+str(text["UAE Dirham"])+"تومن")
    
    def LirPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمت لیر ترکیه"+str(text["Turkish Lira"])+"تومن")
    
    def GoldPrice(self):
        text=Prices().GetSomeInfoAboutPrice()
        Audio().TTS("قیمتِ هر گرم طلای ۱۸ عیارْ "+str(text["Gold 18"])+"تومن")
    
        
class Corona():
    def Statistics(self,Application):
        url="https://www.worldometers.info/coronavirus/"
        r = requests.get(url)
        s = BeautifulSoup(r.text,"html.parser")
        data = s.find_all("div",class_ = "maincounter-number")

        Total_Cases = data[0].text.strip()
        Total_Deaths = data[1].text.strip()
        Total_Recovered = data[2].text.strip()

        if Application=="Total_Cases":
            Audio().TTS("تعداد مبتلیان به کرونا"+' '+(str(Total_Cases).replace(",","")))
            
        if Application=="Total_Deaths":
            Audio().TTS("تعداد مرگ در اثر ابتلا به کرونا"+' '+(str(Total_Deaths).replace(",","")))
            
        if Application=="Total_Recovered":
            Audio().TTS("تعداد بهبودْ یافتگانِ کرونا"+' '+(str(Total_Recovered).replace(",","")))

        return {'Total_Cases' : Total_Cases , 'Total_Deaths' : Total_Deaths , 'Total_Recovered' : Total_Recovered}


class TimingJobs():
    def DoTasksAndCleanFile():
        pass



#print (Data().FindFolders(Data().PWD()+"/Audios"))



#(◕‿◕)
