"""import urllib.request, json 
from pprint import pprint
with urllib.request.urlopen("https://api.tgju.online/v1/data/sana/json") as url:
    data = json.loads(url.read().decode())
    #print(data)
with open("Prices.txt","w") as f:
    f.write(str([*data]))
pprint([(*data)])

DictPrice={}
for i in data:
    #print (i)
    name=data[i]["title"]
    name=name.replace("سامانه سنا","")
    print (name)
    if "فروش" in name:
        name=name.replace("فروش","")
        name=name.replace(" ","")
        DictPrice[name]=data[i]["h"]//10
    
pprint (DictPrice)

with open("Prices.txt","w") as f:
    f.write(str(DictPrice))
"""
from pprint import pprint
import json
import requests
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
pprint (Dic)
with open("Prices.txt","w") as f:
    f.write(str(Dic))