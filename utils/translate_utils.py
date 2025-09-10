from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    return translated

