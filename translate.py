#pip install googletrans, https://pypi.org/project/googletrans/

from googletrans import Translator

translator = Translator()
print(translator.detect('hello world'))

print(translator.translate('おねがいします。'))

