import googletrans
from googletrans import Translator
translator = Translator()
import random
from random import choice


#require user input
needTrans= input ('What do you want to loop translate?')

LANG=[
    'af',
    'am',
    'ar',
    'hy',
    'eu',
    'be',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'ny',
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'en',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'he',
    'hi',
    'hm',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'jw',
    'kn',
    'kk',
    'km',
    'ko',
    'ku',
    'ky',
    'la',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'my',
    'ne',
    'or',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'su',
    'sw',
    'sv',
    'tg',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'ur',
    'ug',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu',
]

x1 = random.choice(LANG)
x2 = random.choice(LANG)
x3 = random.choice(LANG)
x4 = random.choice(LANG)
x5 = random.choice(LANG)
x6 = random.choice(LANG)
x7 = random.choice(LANG)
x8 = random.choice(LANG)
x9 = random.choice(LANG)
x10 = random.choice(LANG)

tranlated1 = translator.translate( needTrans , dest=x1)
tranlated1A = tranlated1.text
print( tranlated1A )

tranlated2 = translator.translate( tranlated1A , dest=x2)
tranlated2A = tranlated2.text
print( tranlated2A )

tranlated3 = translator.translate( tranlated2A , dest=x3)
tranlated3A = tranlated3.text
print( tranlated3A )

tranlated4 = translator.translate( tranlated3A , dest=x4)
tranlated4A = tranlated4.text
print( tranlated4A )

tranlated5 = translator.translate( tranlated4A , dest=x5)
tranlated5A = tranlated5.text
print( tranlated5A )

tranlated6 = translator.translate( tranlated5A , dest=x6)
tranlated6A = tranlated6.text
print( tranlated6A )

tranlated7 = translator.translate( tranlated6A , dest=x7)
tranlated7A = tranlated7.text
print( tranlated7A )

tranlated8 = translator.translate( tranlated7A , dest=x8)
tranlated8A = tranlated8.text
print( tranlated8A )

tranlated9 = translator.translate( tranlated8A , dest=x9)
tranlated9A = tranlated9.text
print( tranlated9A )

tranlated10 = translator.translate( tranlated9A , dest=x10)
tranlated10A = tranlated10.text
print( tranlated10A )


turnback = translator.translate( tranlated10A, dest="en")
turnbackA = turnback.text
print(turnbackA)


