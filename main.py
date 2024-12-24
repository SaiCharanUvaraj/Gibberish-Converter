
import speech_recognition as sr
listener = sr.Recognizer()

from fileHandler import readAllGibbrish,addGibbrish
from speaker import speak
from converter import convertToGibberish

dictionary=readAllGibbrish()
while True:         
    with sr.Microphone() as source:
        print("Speak in english to convert into gibberish...")
        audio = listener.listen(source)
        
    try:
        text = listener.recognize_google(audio)
        print("         You said: " + text)
        
        print("Processing...")
        words=list(text.split())
        gibberish=[]
        for word in words:
            if word in dictionary:
                gibberishWord=dictionary[word]
            else:
                gibberishWord=convertToGibberish(word)
                dictionary[word]=gibberishWord
                addGibbrish(word,gibberishWord)
            gibberish.append(gibberishWord)
        gibberish=" ".join(gibberish)
        print("         Gibberish: " + gibberish)
        
        speak(gibberish)
        
    except sr.UnknownValueError:
        print("         Sorry, your voice is not understandable.")
    except sr.RequestError:
        print("         Sorry, there was an error with the speech recognition service")
    
    print()
    print("Do you want to exit?")
    choice = input("Enter your choice(Yes/No): ").strip().lower()
    if(choice=="yes"):
        print()
        print("Exited successfully...")
        break
    else:
        print()
        print("------------------------------------------------------------------------------------")
