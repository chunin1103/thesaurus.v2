from urllib.request import urlopen
import pyexcel
from word_search import word
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"E:\Projects\..new_chapter_for_thesaurus\Credentials\vi-thesaurus-c8077aebe0c3.json"

ini_url = "https://www.thesaurus.com/browse/"
user_input = word
url = ini_url + user_input
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")

section = soup.find("section", {'class': "css-1e8kf7o-CenterContentContainer e1v16r9g0"})
ul      = section.find("ul", {'class': "css-17d6qyx-WordGridLayoutBox et6tpn80"})
li_list = ul.find_all("li")

symnonym_list = []
for ___ in range(0,8):
    span     = li_list[___].span
    a        = span.a

    symnonym = span.string
    symnonym_list.append(symnonym)


from translate import Translator
translator= Translator(to_lang="vi")


tu_dong_nghia = []
for symnonym in symnonym_list:
    translation = translator.translate(symnonym)
    if translation not in tu_dong_nghia and translation != symnonym:
        tu_dong_nghia.append(translation.capitalize())
print(tu_dong_nghia)
