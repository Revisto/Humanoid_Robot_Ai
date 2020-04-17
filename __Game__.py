from ___Libraries___ import *

class Game():
   
    def Game_Name(self,List):
        Audio().MusicPlay("Click"+"()"+"0.0")
        Input=Audio().GetVoice()
        Audio().MusicPlay("WaitAna"+"()"+"0.0")
        Input=Audio().AnalyseVoice(Input)
        if Input in List:
            List.remove(Input)
        else:
            Audio().TTS("دوباره امتحان کن , یک اسم بگو","fa")
            Audio().MusicPlay("Click"+"()"+"0.0")
            Input=Audio().GetVoice()
            Audio().MusicPlay("WaitAna"+"()"+"0.0")
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
            Audio().MusicPlay("Click"+"()"+"0.0")
            Input=Audio().GetVoice()
            Audio().MusicPlay("WaitAna"+"()"+"0.0")
            Input=Audio().AnalyseVoice(Input)
            if Input in List and Input[0]==MyName[len(MyName)-1]:
                List.remove(Input)
            else:
                Audio().TTS("دوباره تلاش کن","fa")
                Audio().TTS(MyName,"fa")
                Audio().MusicPlay("Click"+"()"+"0.0")
                Input=Audio().GetVoice()
                Audio().MusicPlay("WaitAna"+"()"+"0.0")
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
