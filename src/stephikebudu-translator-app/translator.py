from googletrans import Translator

def translate_to_eng():
  translator = Translator()
  msg = input("Text to translate?: ")
  src_lang = input("Interesting...what language is the text? ")
  dest_lang = input("What language do you want it translated to? ")
  translated_msg = translator.translate(msg, src=src_lang, dest=dest_lang)
  print(f"'{msg}' => '{translated_msg.text}'")

translate_to_eng()