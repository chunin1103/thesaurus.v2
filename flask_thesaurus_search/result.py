from typing import final
from .intersection import final_list
# from googletrans import Translator
# translator = Translator()

# translations = translator.translate(final_list, dest='vi')

# print(translations)
# for translation in translations:
#     print(translation)

from .google_translate_ import *

for i in final_list:
    finalist = translate_text('vi', i)
    print(finalist, end=", ")

