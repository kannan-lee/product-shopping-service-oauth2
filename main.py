import numpy as np
import pyttsx3
from playsound import playsound
import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
#import pocketsphinx
import tkinter as tk

listener = sr.Recognizer()


try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=2)
        print("Set minimum energy threshold to {}".format(listener.energy_threshold))
        print("Say something")
        voice = listener.listen(source)
        with open("output.wav", "wb") as file:
            file.write(voice.get_wav_data())
        playsound("output.wav")
        command= listener.recognize_google(voice,language = 'en-IN', show_all = True)
        command = [c.lower() for c in command]
        print(command)
except Exception as e:
    print(e)