# encoding=utf-8
from gtts import gTTS
import pygame
from pygame import mixer
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts = gTTS(text='哈囉你好啊', lang='zh-tw')
    tts.save('{}.mp3'.format(fp.name))
    mixer.init()
    mixer.music.load('{}.mp3'.format(fp.name))
    mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
