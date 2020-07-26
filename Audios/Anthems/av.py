
import os
mypath="/home/walt/Desktop/__MainAi__/__Ai__/Audios/Anthems/"
Files_Raw = [f for f in os.listdir(mypath)]

#print (Files_Raw)
Folders=[]
Files=[]
for File in Files_Raw:

    if len(File.split("."))==1:
        Folders.append(File)
    else:
        Files.append(File)
print (Files) 
print (Folders)

