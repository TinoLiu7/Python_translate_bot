# encoding=utf-8
import speech_recognition
from gtts import gTTS
import pygame
from pygame import mixer
import tempfile
from googletrans import Translator

def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print('您說的中文是:', r.recognize_google(audio, language='zh-TW'))
    return r.recognize_google(audio, language='zh-TW')

def speak(sentence, lang):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

translator = Translator()
trans_sentence = translator.translate(listenTo(), 'en').text
print('翻譯成英文為:', trans_sentence)
speak(trans_sentence, 'en')

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
