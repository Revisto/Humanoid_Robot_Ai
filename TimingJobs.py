from datetime import datetime

class Time():
    def Time(self):
        Data = (datetime.now())
        print (Data)
        Time = (str(Data).split(" "))[1]
        Time=Time.split(":")
        Time[-1]=(Time[-1].split("."))[0]
        for Parameter in Time:
            Time[Time.index(Parameter)]=int(Parameter)
        return Time

    def Date(self):
        Data = (datetime.now())
        print (Data)
        Date = (str(Data).split(" "))[0]
        Date=Date.split("-")
        for Parameter in Date:
            Date[Date.index(Parameter)]=int(Parameter)
        return Date


def AddFunctionToFile(List):     #for Example [Drug,"str","Lab"]  >>> Timing().Drug("str","Lab")
    FileData=open("Queue.py","a+")
    FileData.write(str(str(List)+","))
    FileData.close()
    
