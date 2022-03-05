import speech_recognition as sr
import pyttsx3
from playsound import playsound
#import pocketsphinx
import tkinter as tk

listener = sr.Recognizer()

if True:
#try:
    with sr.Microphone() as source:
        print("speak something")
        fs = 44100
        voice = listener.listen(source)
        write('output.wav', fs, voice)
        playsound(voice)
        command= listener.recognize_google(voice,language = 'en-IN', show_all = True)
        #command = [c.lower() for c in command]
        print(command)
#except Exception as e:
#    print(e)