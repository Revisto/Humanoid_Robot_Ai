
from Lib.___Local___ import *

def DATA_intents(text):
    Game_List = [
        'هستی']
    
    
    politicsURL = {
        'irna': 'https://www.irna.ir/rss/tp/5',}
    economyURL = {
        'irna': 'https://www.irna.ir/rss/tp/20',}
    worldURL = {
        'irna': 'https://www.irna.ir/rss/tp/1',}
    socialURL = {
        'irna': 'https://www.irna.ir/rss/tp/32',}
    sportsURL = {
        'irna': 'https://www.irna.ir/rss/tp/14',}
    scienceURL = {
        'isna': 'https://www.isna.ir/rss/tp/5',}
    cultureURL = {
        'irna': 'https://www.irna.ir/rss/tp/41',}
    
    
    return {"DATA_intents": [
        
        {"Tag": "Greet",
        "KeyWords": [],
        "KeyWords": ['چطوره', 'احوالت', 'حالت', 'چطوری', 'خوبی', 'حالت خوبه', 'حالت خوب است'],
        "Answers": ["عالی","خوبم","بهتر از این نمیشه","یِکَم خستم","بهترین"],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['اسمت'],
        "Answers": ['من اکبر هستم'],
        "Actions": [],
        },
    
        {"Tag": "Greet",
        "KeyWords": ['کی'],
        "Answers": [' من اکبر هستم.  یک ربات با هوشِ مصنوعیِ قوی و آماده خدمتِ به شما'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['چی کار', 'چیکار'],
        "Answers": ['من هر کاری که نیاز داشته باشی رُ میتونم انجام بدم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['ساخته', 'ساختن',"ساخت"],
        "Answers": ['آقایان علیرضا شعبانی و پارسا سلیمانی'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['درود بر شما', 'درود', 'سلام', 'سلامٌ عَلِیکُم', 'درود فراوان', 'سلام بر تو باد', 'درودِ فراوان', 'سلام'],
        "Answers": ['درود بر شما', 'درود', 'سلام', 'سلامٌ عَلِیکُم', 'سلام بر تو باد', 'درودِ فراوان'],
        "Actions": [],
        },

        {"Tag": "Play",
        "KeyWords": ['سوره', 'قران', 'قرآن'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(["Sooreh_1"])),text]],
        },
    
        {"Tag": "Play",
        "KeyWords": ['اذان', 'ازان'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,((random.choice(["Azan"])),text)]],
        },

        {"Tag": "Play",
        "KeyWords": ['بهنام', 'بانی','موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("‌BehnamBani",1)),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['حامد', 'بهرام','موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("HamedBahram",1)),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['آرون', 'افشار','موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("AronAfshar",1)),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['ترکیه', 'ترکیه','موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("Turkish",1)),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['گیتار', 'جیپسی', 'فلامینگو','موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("Gypsy",1)),text]],
        },
        {"Tag": "Play",
        "KeyWords": ['جهان بخش', 'جهانبخش', 'بابک','موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("BabakJahanbakhsh",1)),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['موزیک', 'آهنگ', 'اهنگ'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(Audio().AllMusicsList())),text]],
        },

        {"Tag": "Greet",
        "KeyWords": ['پسری', 'پسر هستی', 'دختری', 'دختر هستی', 'جنسیت'],
        "Answers": ['من یک ربات هستم ولی اسمِ من پسرانه است'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['چند سال', 'به دنیا', 'تولد', 'سن'],
        "Answers": ['من کمتر از یک سال دارم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords":['عشقم', 'عزیزم', 'خوشم میاد', 'عاشقتم', 'دوستت دارم', 'تورو دوست دارم', 'شمارو دوست دارم'],
        "Answers": ['من هم شما رو دوست دارم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['چه کاری علاقه داری', 'چه کاری لذت میبری', 'چه کاری خوشت میاد', 'چه کاری رو دوست داری', 'چه کاری را دوست داری', 'چه کاری دوست داری'],
        "Answers": ['من عاشقِ باطری هستم و همیشه دوست دارم باطری اِستِعمال کنم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "KeyWords": ['رنگ', 'رنگی'],
        "Answers": ['من عاشق رنگِ سفید هستم'],
        "Actions": [],
        },

        {"Tag": "Date",
        "KeyWords": ['چند شنبه'],
        "Answers": [],
        "Actions": [[DateAndWeather().Day]],
        },

        {"Tag": "Date",
        "KeyWords": ['چندم', 'تاریخ'],
        "Answers": [],
        "Actions": [[DateAndWeather().Date]],
        },

        {"Tag": "Date",
        "KeyWords": ['ساعت','چند'],
        "Answers": [],
        "Actions": [[DateAndWeather().Time_Now]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر فرهگ', 'اخبار فرهگ', 'خبر هنر', 'اخبار هنر'],
        "Answers": [],
        "Actions": [[Others().News,cultureURL]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر علم', 'اخبار علمی', 'خبر دانش', 'اخبار دانش'],
        "Answers": [],
        "Actions": [[Others().News,scienceURL]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر ورزش', 'اخبار ورزشی'],
        "Answers": [],
        "Actions": [[Others().News,sportsURL]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر اجتماع', 'اخبار اجتماع'],
        "Answers": [],
        "Actions": [[Others().News,socialURL]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر جهان', 'اخبار جهان'],
        "Answers": [],
        "Actions": [[Others().News,worldURL]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر اقتصاد', 'اخبار اقتصاد'],
        "Answers": [],
        "Actions": [[Others().News,economyURL]],
        },

        {"Tag": "News",
        "KeyWords": ['خبر سیاس', 'اخبار سیاس'],
        "Answers": [],
        "Actions": [[Others().News,politicsURL]],
        },

        {"Tag": "News",
        "KeyWords": ['اخبار'],
        "Answers": [],
        "Actions": [[Others().News,random.choice([sportsURL,socialURL,worldURL,economyURL,politicsURL,cultureURL,scienceURL])]],
        },

        {"Tag": "Price",
        "KeyWords": ['طلا'],
        "Answers": [],
        "Actions": [[Prices().GoldPrice]],
        },

        {"Tag": "Price",
        "KeyWords": ['ربع سکه'],
        "Answers": [],
        "Actions": [[Prices().RobCoin]],
        },

        {"Tag": "Price",
        "KeyWords": ['نیم سکه'],
        "Answers": [],
        "Actions": [[Prices().HalfCoinPrice]],
        },

        {"Tag": "Price",
        "KeyWords": ['تمام سکه', 'سکه تمام'],
        "Answers": [],
        "Actions": [[Prices().FullCoinPrice]],
        },

        {"Tag": "Price",
        "KeyWords": ['دلار'],
        "Answers": [],
        "Actions": [[Prices().DollarPrice]],
        },

        {"Tag": "Price",
        "KeyWords": ['یورو'],
        "Answers": [],
        "Actions": [[Prices().EuroPrice]],
        },

        {"Tag": "Price",
        "KeyWords": ['پوند'] ,
        "Answers": [],
        "Actions": [[Prices().PondPrice]],
        },

        {"Tag": "Price",
        "KeyWords": ['درهم'] ,
        "Answers": [],
        "Actions": [[Prices().DerhamPrice]],
        },


        {"Tag": "Price",
        "KeyWords": ['لیر'] ,
        "Answers": [],
        "Actions": [[Prices().LirPrice]],
        },

        {"Tag": "Calculation",
        "KeyWords": ['جواب', 'مجموع', 'حاصل'] ,
        "Answers": [],
        "Actions": [[Others().Calculater,text]],
        },

        {"Tag": "Weather",
        "KeyWords": ['هوا', 'دما', 'باد'] ,
        "Answers": [],
        "Actions": [[DateAndWeather().Temperature,text]],
        },

        {"Tag": "Fun",
        "KeyWords": ['جک', 'جوک'] ,
        "Answers": [],
        "Actions": [[Others().Joke]],
        },

        {"Tag": "Internet",
        "KeyWords": ['سرچ', 'جست و جو', 'جستجو'] ,
        "Answers": [],
        "Actions": [[Data().Search,str(text)]],
        },

        {"Tag": "Play",
        "KeyWords": ['پادکست'] ,
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(["Podcast"])),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['شعر', 'اخوان', 'دکلمه', 'باغ بی برگی'] ,
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(["BaghBiBargi"])),text]],
        },

        {"Tag": "Play",
        "KeyWords": ['سرود'] ,
        "Answers": [],
        "Actions": [[Audio().Anthems,text]],
        },
        
        {"Tag": "Corona",
        "KeyWords": ['آمار','تعداد','قربان','کشته','مرد','مرگ','کرونا','کووید'] ,
        "Answers": [],
        "Actions": [[Corona().Statistics,"Total_Deaths"]],
        },
        
        {"Tag": "Corona",
        "KeyWords": ['آمار','تعداد','شناسایی','مبتلا','گرفت','کرونا','کووید'] ,
        "Answers": [],
        "Actions": [[Corona().Statistics,"Total_Cases"]],
        },
        
        {"Tag": "Corona",
        "KeyWords": ['آمار','تعداد','بازگشت','بهبود','کرونا','کووید']  ,
        "Answers": [],
        "Actions": [[Corona().Statistics,"Total_Recovered"]],
        },
        
        ]
    }

