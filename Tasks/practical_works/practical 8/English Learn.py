import pymorphy2
import translate

morph = pymorphy2.MorphAnalyzer()
translator = translate.Translator(from_lang='ru', to_lang='en')


