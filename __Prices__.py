from ___Libraries___ import *

class Prices():
    def GetSomeInfoAboutPrice(self):
        url = "https://www.iranjib.ir/showgroup/23/realtime_price/"
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        return text
    
    def RobCoin(self,text):
        Audio().TTS((text[(text.index("  ربع سکه"))+3])+"ریال","fa")
    
    def HalfCoinPrice(self,text):
        Audio().TTS((text[(text.index("  نیم سکه"))+3])+"ریال","fa")
    
    def FullCoinPrice(self,text):
        Audio().TTS((text[(text.index("  طرح جدید"))+3])+"ریال","fa")
    
    def DollarPrice(self,text):
        Audio().TTS((text[(text.index("  قیمت دلار"))+3])+"ریال","fa")
    
    def EuroPrice(self,text):
        Audio().TTS((text[(text.index("  قیمت یورو"))+3])+"ریال","fa")
    
    def PondPrice(self,text):
        Audio().TTS((text[(text.index("  قیمت پوند انگلیس"))+3])+"ریال","fa")
    
    def DerhamPrice(self,text):
        Audio().TTS((text[(text.index("  قیمت درهم"))+3])+"ریال","fa")
    
    def LirPrice(self,text):
        Audio().TTS((text[(text.index("  قیمت لیر ترکیه"))+3])+"ریال","fa")
    
    def GoldPrice(self,text):
        Audio().TTS((text[(text.index("  هر گرم طلای 18 عیار"))+3])+"ریال","fa")
    
    def BitCoinPrice(self,text):
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
        Audio().TTS(str(Rial)+"ریال","fa")
