from gtts import gTTS
from subprocess import call
from playsound import playsound

def criar_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/bem_vindo.mp3')
    #call('afplay','audios/hello.mp3') #OSX
    #call('aplay','audios/hello.mp3')  #LINUX
    playsound('bem_vindo.mp3')  # WINDONS

criar_audio('Oi, eu sou a Rose.')