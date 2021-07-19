from urllib.request import urlopen
from .input_word import word
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"E:\Projects\.new_chapter_for_thesaurus\Credentials\vi-thesaurus-c8077aebe0c3.json"

ini_url = "https://www.thesaurus.com/browse/"
user_input = word.replace('-', '%20')
url = ini_url + user_input
from bs4 import BeautifulSoup

try:
    conn = urlopen(url)
    urlopen(url)
    raw_data = conn.read()
    webpage_text = raw_data.decode("utf-8")
    soup = BeautifulSoup(webpage_text, "html.parser")

    section = soup.find("section", {'class': "css-1fzg0m e1v16r9g0"})
    ul      = section.find("div", {'class': "css-ixatld e1cc71bi0"})
    li_list = ul.find_all("li")

    symnonym_list = []
    for __ in li_list:
        word_crawled = __.text.strip()
        symnonym_list.append(word_crawled)

    print(symnonym_list)
except:
    print('shit')
