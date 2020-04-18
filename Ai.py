"""
 ███╗   ███╗  █████╗  ██╗ ███╗   ██╗ ██╗ 
 ████╗ ████║ ██╔══██╗ ██║ ████╗  ██║ ██║ 
 ██╔████╔██║ ███████║ ██║ ██╔██╗ ██║ ██║ 
 ██║╚██╔╝██║ ██╔══██║ ██║ ██║╚██╗██║ ╚═╝ 
 ██║ ╚═╝ ██║ ██║  ██║ ██║ ██║ ╚████║ ██╗ 
 ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝ 
"""

from imp import reload
#-----L I B R A R I E S-----
from Libraries.___Local___ import *
import ___DataBase___ 
#-----L  O  C  A   L-----


Audio().TTS("در خدمتم","fa")

while True:
    reload(___DataBase___)
    text=Audio().CompleteVoiceAnalyse()
    #text = input("text=")
    if 'خاموش' in text:
        while 'روشن' not in text or 'بیدار' not in text:
            text=Audio().CompleteVoiceAnalysMute()

    elif Data().WHQ(text) and text!="" and Data().Analyse_Closest(text,___DataBase___.DataBase):
        None
    
    
    elif not(Data().Analyse_Function(text,Data().DATA_function(text))) and text!="":
        Data().AddToDataBase(text)
        #IDK() 

    elif text!="":
        Data().AddToDataBase(text)



"""
 ██████╗  ███████╗ ██╗   ██╗ ██╗ ███████╗ ████████╗  ██████╗  
 ██╔══██╗ ██╔════╝ ██║   ██║ ██║ ██╔════╝ ╚══██╔══╝ ██╔═══██╗ 
 ██████╔╝ █████╗   ██║   ██║ ██║ ███████╗    ██║    ██║   ██║ 
 ██╔══██╗ ██╔══╝   ╚██╗ ██╔╝ ██║ ╚════██║    ██║    ██║   ██║ 
 ██║  ██║ ███████╗  ╚████╔╝  ██║ ███████║    ██║    ╚██████╔╝ 
 ╚═╝  ╚═╝ ╚══════╝   ╚═══╝   ╚═╝ ╚══════╝    ╚═╝     ╚═════╝ 
"""