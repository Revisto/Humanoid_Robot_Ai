from ___Libraries___ import *

class Audio():
    def MusicPlay(self,RareInput):
        MusicName,text=RareInput.split("()")
        print (MusicName,text)
        player = MPyg321Player()       # instanciate the player
        Locations=["/Audios/Songs/","/Audios/Talks/","/Audios/Splitter Voices/","/Audios/Anthems/","/Audios/Podcasts/","/Audios/Poems/"]
        Pwd=(str(Data().PWD()))
        for Loc in Locations:
            Path=Pwd+Loc+MusicName+".mp3"
            if os.path.exists(Path):
                print (Path)
                player.play_song(Path)
                break

        time.sleep(Audio().FindHowMuchToPlay(Path,text))               
        player.quit()  
    
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
                    Audio().MusicPlay(list_en[list_fa.index(Box)]+"()"+text)
                    return 
        
        Audio().TTS(random.choice(["پیدا نکردم","تو انبار نداریم"]),"fa")
    
    def CompleteVoiceAnalyse(self):
        try:
            Audio().MusicPlay("Click"+"()"+"0.0")
            audio = Audio().GetVoice()
            Audio().MusicPlay("WaitAna"+"()"+"0.0")
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
        doc = requests.get("http://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=C6QAXK7BNFEI10M&Text="+TEXT+"&Speaker=Male1&Format=mp3&GainLevel=0&PitchLevel=0&PunctuationLevel=0&SpeechSpeedLevel=-10&ToneLevel=0&Quality=normal&BeginningSilence=0&EndingSilence=0&Base64Encode=0")
        with open(Data().PWD()+"/Audios/Talks/"+'Talk.mp3', 'wb') as f:
            f.write(doc.content)
        Audio().MusicPlay("Talk"+"()کامل")
    
    def CompleteVoiceAnalysMute(self):
        try:
            audio = GetVoice()
            text = AnalyseVoice(audio)
        except:
            text=""
        return text
    
    def IDK(self):
        Audio().TTS(random.choice(["متاسفانه متوجهِ منظورتون نِمیشم","متاسفانه متوجه نَشدم","شرمنده متوجه منظورتون نِمیشم","شرمنده متوجهِ نشدم","من دارم یاد میگیرم و متوجهِ منظورتون نِمیشم","متاسفانه نفهمیدم"]),"fa")      
