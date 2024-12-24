import pyttsx3
speaker = pyttsx3.init()

def speak(text):
    speaker.setProperty('rate', 125)  
    speaker.setProperty('volume', 1) 
    speaker.say(text)
    speaker.runAndWait()