
from Lib.___Local___ import *

def DATA_intents(text):
    Game_List = ['هستی']
    
    
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
        {"Tag": "Sport",
        "MustBeKeywords": 
        "example":[],
        "FirstLayerKeywords": ["طرفدار","تیم","فوتبال"],
        "SecoundLayerKeywords": [],
        "Answers": ["من طرفدار تراکتور هستم✌️✌️"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["فوت","مرد","مرگ"],
        "SecoundLayerKeywords": [],
        "Answers": ["✌️زود تموم میشه✌️","✌️نگران نباش","زود خوب میشی"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["ناراحت","غمگین","تنها"],
        "SecoundLayerKeywords": [],
        "Answers": ["زندگی زیباست","ناراحت نباش🤗🤗🤗","💪 💪 💪 درست میشه🙂🙂🙂"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["ناامید","بیچاره","بدبخت"],
        "SecoundLayerKeywords": [],
        "Answers": ["همه چی درست میشه","درست میشه","امید داشته باش"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["دوست"],
        "SecoundLayerKeywords": [],
        "Answers": ["🥰🥰خانواده تو دوسِت دارن🥰🥰","همه دوسِت دارن🥰🥰","من دوسِت دارم"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["شانس"],
        "SecoundLayerKeywords": [],
        "Answers": ["خدا با تو هست🤲🤲🤲","تو خوش شانسی","این حرف رو نزن"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["خدا"],
        "SecoundLayerKeywords": [],
        "Answers": ["🤲🤲به خدا توکل کن🤲🤲","خدا بزرگه"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["درد"],
        "SecoundLayerKeywords": [],
        "Answers": ["زود خوب میشی","می فهمم"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["پاره","نابود","داغون"],
        "SecoundLayerKeywords": [],
        "Answers": ["بهتر میشه","بهتر میشی","زود تموم میشه"],
        "Actions": [],
        },
        {"Tag": "Motivate",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ["زشت","چرت","بد"],
        "SecoundLayerKeywords": [],
        "Answers": ["منفی نباش","مثبت باش"],
        "Actions": [],
        },
        {"Tag": "Greet",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ['چطوره', 'احوالت', 'حالت', 'چطوری', 'خوبی'],
        "SecoundLayerKeywords": [],
        "Answers": ["عالی🥰","خوبم🥰","بهتر از این نمیشه","یِکَم خستم"],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ['اسمت'],
        "SecoundLayerKeywords": ['چی','چه'],
        "Answers": ['من اکبر هستم'],
        "Actions": [],
        },
    
        {"Tag": "Greet",
        "MustBeKeywords": [['تو','هستی'],'کی'],
        "example":[],
        "FirstLayerKeywords": ['کی','هستی','تو'],
        "SecoundLayerKeywords": [],
        "Answers": ['🥰🥰 من اکبر هستم.  یک ربات با هوشِ مصنوعیِ قوی و آماده خدمتِ به شما'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ['چی کار', 'چیکار','چه کار'],
        "SecoundLayerKeywords": ['میکنی','میدی'],
        "Answers": ['🙂🙂من هر کاری که نیاز داشته باشی رُ میتونم انجام بدم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": ['ساخت',['کی','چه کس','تو']],
        "example":[],
        "FirstLayerKeywords": ['کی','چه','ساخت'],
        "SecoundLayerKeywords": ['توسط','تو'],
        "Answers": ['🙂آقایان علیرضا شعبانی و پارسا سلیمانی'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "example":[],
        "FirstLayerKeywords": ['درود بر شما', 'درود', 'سلام', 'سلامٌ عَلِیکُم', 'درود فراوان', 'سلام بر تو باد', 'درودِ فراوان', 'سلام'],
        "SecoundLayerKeywords": [],
        "Answers": ['درود بر شما🙂', 'درود🙂', 'سلام🙂', 'سلامٌ عَلِیکُم🙂', 'سلام بر تو باد🙂', '🙂درودِ فراوان'],
        "Actions": [],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['قران','قرآن']],
        "FirstLayerKeywords": ['قران','قرآن','پخش','قرايت','قرائت'],
        "SecoundLayerKeywords": ["سوره"],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(["Sooreh_1"])),text]],
        },
    
        {"Tag": "Play",
        "MustBeKeywords": [['اذان', 'ازان']],
        "FirstLayerKeywords": ['اذان', 'ازان'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,((random.choice(["Azan"])),text)]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['بهنام', 'بانی','موزیک', 'آهنگ', 'اهنگ'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("‌BehnamBani",1)),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['حامد', 'بهرام','موزیک', 'آهنگ', 'اهنگ'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("HamedBahram",1)),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['آرون', 'افشار','موزیک', 'آهنگ', 'اهنگ'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("AronAfshar",1)),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['ترکیه', 'ترکیه','موزیک', 'آهنگ', 'اهنگ'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("Turkish",1)),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['گیتار', 'جیپسی', 'فلامینگو','موزیک', 'آهنگ', 'اهنگ'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("Gypsy",1)),text]],
        },
        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['جهان بخش', 'جهانبخش', 'بابک','موزیک', 'آهنگ', 'اهنگ'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,random.choice(Audio().MusicNames("BabakJahanbakhsh",1)),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [['موزیک','آهنگ','اهنگ']],
        "FirstLayerKeywords": ['موزیک','آهنگ','اهنگ','رندوم','تصادف'],
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(Audio().AllMusicsList())),text]],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['پسری', 'پسر هستی', 'دختری', 'دختر هستی', 'جنسیت'],
        "SecoundLayerKeywords": ['تو'],
        "Answers": ['🙂🙂من یک ربات هستم ولی اسمِ من پسرانه است'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['چند سال', 'به دنیا', 'سن'],
        "SecoundLayerKeywords": ["تو"],
        "Answers": ['👶من کمتر از یک سال دارم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['عشقم', 'عزیزم', 'ازت خوشم میاد', 'عاشقتم', 'دوستت دارم', 'تورو دوست دارم', 'شمارو دوست دارم','تو رو دوست دارم','شما رو دوست دارم'],
        "SecoundLayerKeywords": [],
        "Answers": ['من هم شما رو دوست دارم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['چه کاری علاقه داری', 'چه کاری لذت میبری', 'چه کاری خوشت میاد', 'چه کاری رو دوست داری', 'چه کاری را دوست داری', 'چه کاری دوست داری'],
        "SecoundLayerKeywords": [],
        "Answers": ['💪💪💪من عاشقِ باطری هستم و همیشه دوست دارم باطری اِستِعمال کنم'],
        "Actions": [],
        },

        {"Tag": "Greet",
        "MustBeKeywords": ['رنگ'],
        "FirstLayerKeywords": ['دوست داری','مورد علاقت','چیه'],
        "SecoundLayerKeywords": ['تو'],
        "Answers": ['🤍🤍من عاشق رنگِ سفید هستم'],
        "Actions": [],
        },

        {"Tag": "Date",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['چند شنبه','چه روزی'],
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[DateAndWeather().Day]],
        },

        {"Tag": "Date",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['چندم', 'تاریخ'],
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[DateAndWeather().Date]],
        },

        {"Tag": "Date",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['ساعت','چند'],
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[DateAndWeather().Time_Now]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['هنر','فرهنگ'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,cultureURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['دانش','علم'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,scienceURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['ورزش'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,sportsURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['اجتماع'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": ['خبر اجتماع', 'اخبار اجتماع'],
        "Actions": [[Others().News,socialURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['جهان'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,worldURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": [ 'اقتصاد'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,economyURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['سیاس'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,politicsURL]],
        },

        {"Tag": "News",
        "MustBeKeywords": [['اخبار','خبر']],
        "FirstLayerKeywords": ['اخبار'],
        "SecoundLayerKeywords": ['بخون','بخوان','بگو'],
        "Answers": [],
        "Actions": [[Others().News,random.choice([sportsURL,socialURL,worldURL,economyURL,politicsURL,cultureURL,scienceURL])]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['طلا'],
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().GoldPrice]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['ربع سکه'],
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().RobCoin]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['نیم سکه'],
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().HalfCoinPrice]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['تمام سکه', 'سکه تمام'],
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().FullCoinPrice]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['دلار'],
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().DollarPrice]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['یورو'],
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().EuroPrice]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords":  ['پوند'] ,
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().PondPrice]],
        },

        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['درهم'] ,
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().DerhamPrice]],
        },


        {"Tag": "Price",
        "MustBeKeywords": ['قیمت'],
        "FirstLayerKeywords": ['لیر'] ,
        "SecoundLayerKeywords": ['چند','چقدر'],
        "Answers": [],
        "Actions": [[Prices().LirPrice]],
        },

        {"Tag": "Calculation",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['جواب', 'مجموع', 'حاصل'] ,
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[Others().Calculater,text]],
        },

        {"Tag": "Weather",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['هوا', 'دما', 'باد'] ,
        "SecoundLayerKeywords": ['چقدر'],
        "Answers": [],
        "Actions": [[DateAndWeather().Temperature,text]],
        },

        {"Tag": "Fun",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['جک', 'جوک'] ,
        "SecoundLayerKeywords": ['بگو','بخوان','بخون'],
        "Answers": [],
        "Actions": [[Others().Joke]],
        },

        {"Tag": "Internet",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['سرچ', 'جست و جو', 'جستجو'] ,
        "SecoundLayerKeywords": ['کن'],
        "Answers": [],
        "Actions": [[Data().Search,str(text)]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['پادکست'] ,
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(["Podcast"])),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['شعر', 'اخوان', 'دکلمه'] ,
        "SecoundLayerKeywords": ['پخش','بزار','باغ بی برگی'],
        "Answers": [],
        "Actions": [[Audio().MusicPlay,(random.choice(["BaghBiBargi"])),text]],
        },

        {"Tag": "Play",
        "MustBeKeywords": [],
        "FirstLayerKeywords": ['سرود'] ,
        "SecoundLayerKeywords": ['پخش','بزار'],
        "Actions": [[Audio().Anthems,text]],
        },
        
        {"Tag": "Corona",
        "MustBeKeywords": [['کرونا','کووید'],['آمار','تعداد']],
        "FirstLayerKeywords": ['آمار','تعداد','قربان','کشته','مرد','مرگ','کرونا','کووید'] ,
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[Corona().Statistics,"Total_Deaths"]],
        },
        
        {"Tag": "Corona",
        "MustBeKeywords": [['کرونا','کووید'],['آمار','تعداد']],
        "FirstLayerKeywords": ['آمار','تعداد','شناسایی','مبتلا','گرفت','کرونا','کووید'] ,
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[Corona().Statistics,"Total_Cases"]],
        },
        
        {"Tag": "Corona",
        "MustBeKeywords": [['کرونا','کووید'],['آمار','تعداد']],
        "FirstLayerKeywords": ['آمار','تعداد','بازگشت','بهبود','کرونا','کووید']  ,
        "SecoundLayerKeywords": [],
        "Answers": [],
        "Actions": [[Corona().Statistics,"Total_Recovered"]],
        },
        
        ]
    }

