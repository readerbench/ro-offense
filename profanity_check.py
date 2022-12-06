import re

profanity_list = [
    "laba", 
    "ce pula",
    "ce pizda",
    "caca",
    "cacat",
    "cacao",
    "pipi",
    "pisat",
    "pishat",
    "rahat",
    "kkt",
    "kk",
    "plm",
    "ma fut",
    "ma cac",
    "ma pis",
    "ma pish",
    "pwla",
    "p.u.l.a.",
    "poola",
    "naiba",
    "dracu",
    "draq",
    "drecu",
    "naibii",
    "dracului",
    "drecului",
    "drqlui",
    "coaie",
    "coae",
    "sloboz",
    "lindic",
    "gaoz",
    "ochiul maro",
    "floci",
    "cur",
    "futai",
    "futare",
    "futere",
    "popou",
    "nanau",
    
]

abuse_list = [
    "tigan(|u|ilor|ul|i|ii)", 
    "tzigan(|u|ilor|ul|i|ii)",
    "cretin(|u|ilor|ul|i|ii)",
    "idiot(|u|ilor|ul|i|ii)",
    "oligofren(|u|ilor|ul|i|ii)",
    "retardat(|u|ilor|ul|i|ii)",
    "handicapat(|u|ilor|ul|i|ii)",
    "taran(|u|ilor|ul|i|ii)",
    "cioban(|u|ilor|ul|i|ii)",
    "tzaran(|u|ilor|ul|i|ii)",
    "poponar(|u|ilor|ul|i|ii)",
    "bulangiu(|ilor|l|i|ii)",
    "curv(a|ele|elor)",
    "va fut(|em)",
    "te fut(|em)",
    "mort(|i|ii)",
    "mortz(|i|ii)",
    "ma-ta",
    "mata",
    "mue",
    "muie",
    "labar(|u|i|ii|ilor)",
    "labagi(|lor|ilor|i|u|l)",
    "nenorocit(|u|ilor|ul|i|ii)",
    "tampit(|u|ilor|ul|i|ii)",
    "timpit(|u|ilor|ul|i|ii)",
    "bou(|ul|i|ii)",
    "prost(|u|ilor|ul|i|ii)",
    "proast(|elor|a|ele)",
    "fute in cur",
    "futuva",
    "aurolac(|u|ilor|i|ul)",
    "papagal(|u|i|ilor|ule)",
    "fraier(|u|ilor|i|ii)",
    "futu-va(|\-n)",
    "penibil(|u|ilor|i|ii)",
    "ma cac pe",
    "ma pis pe",
    "ma pish pe",
    "jigod(|ia|iilor|ilor|ie|i|ii)",
    "nebun(|u|ilor|a|ul|i|ii)",
    "sug(i|eti) (pula|pwla|poola)",
    "in cur pe",
    "in pula pe",
    "cacanar(|u|i|ii|ilor)",
    "nesimtit(|u|o|i|ii|ilor)",
    "e de cacat",
    "e de rahat",
    "e de kkt",
    "e de kk",
    "ciori(|le)",
    "cioara",
    "javr(|a|e)",
    "fmm",
    "caca-ne am",
    "popo(.*)",
    "homo(.*)",
    "porc(|ul|ii|i)",
    "gunoi de",
    "suge pula",
    "jidan(|i|ii|ul)",
    "imbecil(|i|ii|ul)",
    "bozgor(|i|ii|ilor|e|ul|u)",
    "tembel(|i|ii|ilor|ule|u|ul)",
    "ungur(|i|ii|ul)",
    "magar(|i|ii|u|ul)",
    "retar(|d|zi|dul|dule|zilor)",
    "zdreant(|z)(|a|o)",
    "gras(|u|ul|ule)",
    "sa mor(|i)",
    
]

profanity_list = [x.replace(" ",r"\s") for x in profanity_list]
abuse_list = [x.replace(" ",r"\s") for x in abuse_list]


def profanity_check(comment):

    if not isinstance(comment,str): return 0
        
    text = comment.lower() 
    prof_list = "|".join(profanity_list)
    abus_list = "|".join(abuse_list)
    
    has_profanity = re.search(rf"\b({prof_list})\b", text) is not None
    has_abuse =  re.search(rf"\b({abus_list})\b", text) is not None
    
    
    return {'has_profanity':1 if has_profanity else 0, 'has_abuse':1 if  has_abuse else 0}
