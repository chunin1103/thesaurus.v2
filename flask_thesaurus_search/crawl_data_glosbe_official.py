from urllib.request import urlopen
from collections import OrderedDict
from .input_word import word

ini_url = "https://vi.glosbe.com/en/vi/"
url     = ini_url + word
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")

div1        = soup.find("main",{'class': 'flex-1 px-1 md:px-2'})
words       = div1.find("ul",{'class': 'translations__list'})

symnonym_list_glosbe = []

div      = words.find_all("span", {'class': 'translation__item__phrase'})
for wordies in div:
    if wordies is not None:
        span_long = wordies.span.text
        # result: ['\n\năn\n\n', '\n\năn cơm\n\n', '\n\nnhá\n\n']
        # Cần lọc thêm
        spann      = span_long.replace('\n', '')
        symnonym_list_glosbe.append(spann)
print(symnonym_list_glosbe)
