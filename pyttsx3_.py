

# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline,


import pyttsx3


engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()