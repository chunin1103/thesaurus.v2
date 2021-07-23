from typing import Text
from .google_translate_ import *

word = input(str)
word = translate_text('en', word)
word = word.strip()
word = word.replace(' ', '-')

print(word)