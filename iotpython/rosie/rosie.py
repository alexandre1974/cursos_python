import speech_recognition as sr

# obtain audio from the microphone
microfone = sr.Recognizer()
with sr.Microphone() as source:
    print("Aguardando comando")
    audio = microfone.listen(source)
# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said " + microfone.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
