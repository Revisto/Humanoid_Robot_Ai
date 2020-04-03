from __rOBOT_fUNCTIONS__ import *

PricesInfo=GetSomeInfoAboutPrice()
TTS("در خدمتم ","fa")
Status="Done"
while True:
    Status=WakeUp(TimeMustWakeUp,Time_Now_For_WakeUp(),Status)
    RimindReminders(ReturnAllReminders(),Time_Now_For_WakeUp())
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