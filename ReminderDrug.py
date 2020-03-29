Reminders=open("Reminders.py","r+")
def ReturnAllReminders():
    All=[]
    for i in range (len(Reminders.read())):
        All.append(i)
    return()
a= (Reminders.read())
print (a[0])
"""def AddToReminder():

def DeleteFromReminder():

def RimindReminders():"""