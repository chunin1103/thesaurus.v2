import requests
import collections
from translate import Translator
from word_search import word

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"E:\Projects\..new_chapter_for_thesaurus\Credentials\vi-thesaurus-c8077aebe0c3.json"
translator= Translator(to_lang="vi")

ini_url = "https://api.onelook.com/words?v=ol_gte3&ml=%20{{ u }}&qe=ml&md=dp&max=1000&k=olthes_r4"
url = ini_url.replace("{{ u }}", word)
r = requests.get(url)
data = r.json()

tu_dong_nghia =[]
for _ in range (0, 25):
    if data[_]['word'] is not None:
        tu_dong_nghia.append(data[_]['word'])

ds_tu_dong_nghia=[]

from google.cloud import translate_v2 as translate
translate_client = translate.Client()
target = 'vi'

for word in tu_dong_nghia:
        translation = translate_client.translate(
        word,
        target_language=target)
        if translation != word.capitalize():
                ds_tu_dong_nghia.append(translation['translatedText'].capitalize())
print(ds_tu_dong_nghia)

for word in tu_dong_nghia:
    translation = translator.translate(word)
    if translation != word and translation.capitalize() not in ds_tu_dong_nghia:
        ds_tu_dong_nghia.append(translation.capitalize())

print(tu_dong_nghia)


