from urllib.request import urlopen
from collections import OrderedDict
from word_search import word

ini_url = "https://vi.glosbe.com/en/vi/"
url     = ini_url + word
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")

div1        = soup.find("section",{'class': 'translate-entry-translations'})
div_list    = div1.find_all("h4", {'lang': 'vi'})

div2        = soup.find("div", {'class': 'translate-entry-others-text'})
div2_list   = div2.find_all("span", {'class': 'ng-star-inserted'})

symnomym_list = []
for div in div_list:
    symnonym = div.string
    if symnonym is not None:
        symnomym_list.append(symnonym.capitalize())

for div in div2_list:
    symnonym = div.string
    if symnonym is not None:
        symnomym_list.append(symnonym.capitalize())

print(symnomym_list)
