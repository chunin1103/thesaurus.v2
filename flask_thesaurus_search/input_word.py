from typing import Text
from .google_translate_ import *
# from .routes import key_word

word = input(str)
# word = key_word
word = translate_text('en', word)
word = word.strip()
word = word.replace(' ', '-')

print(word)