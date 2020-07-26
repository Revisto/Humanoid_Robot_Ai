
#-----L I B R A R I E S-----
#-----------A  U  D  I  O----------
#------D  A  T  A-------
#-----DATE and Weather
#-------G   a    m    e   s---------
#---------P r i c e s------------
#------Timing J O B S----------
#-------O th e r s-----------

"""
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
"""
