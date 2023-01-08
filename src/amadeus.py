import pyaudio
import speech_recognition as sr
import pyttsx3 as speaking
import datetime
import os
import webbrowser

def takecommand():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        audio = mic.listen(source)
    try :
        query = mic.recognize_google(audio,language="en-in")
        print(f"Nilesh : {query}")
    except Exception as e:
        print(e)
    return query

def speak(str):
    engine = speaking.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(str)
    engine.runAndWait()

def wish():    
    hour = int(datetime.datetime.now().hour)
    if hour < 6 :
        speak("Good Evening,")
    elif hour > 6 and hour < 12 :
        speak("Good Morning,")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon,")
    elif hour > 16 :
        speak("Good Evening,")
    speak("Hello Nilesh I am Amadeus your desktop assistant. you can call me Ammy. Please tell me how may i help you?")
    
def wtime():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    day="AM"
    if (hour>12):
        hour=hour - 12
        day="PM"
    print(f"Amadeus : Nilesh,It's {hour} {minute} {day}")
    speak(f"Nilesh,It's {hour} {minute} {day}")



if __name__=="__main__":  
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    wish() 
    while True:
        try:
            command = takecommand().lower()
            if ("bye" in command) or ("quit" in command) or ("exit" in command) or ("close" in command):
                print("Amadeus : Okay Nilesh see you then")
                speak("Okay Nilesh see you then")
                exit()

            if ("code" in command):
                print("Amadeus : Okay opening VS code...")
                speak("Okay opening VS code")
                os.startfile("C:\\Users\\Nilesh\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")

            if ("file" in command):
                print("Amadeus : Okay opening file explorer...")
                speak("Okay opening file explorer.")
                os.startfile("C:\\Windows\\explorer.exe")

            if ("note" in command):
                print("Amadeus : Okay opening Notepad...")
                speak("Okay opening Notepad.")
                os.startfile("C:\\Windows\\notepad.exe")

            if ("firefox" in command):
                print("Amadeus : Okay opening Firefox...")
                speak("Okay opening Firefox.")
                firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                firefox.open('http://www.google.com')

            if ("youtube" in command):
                print("Amadeus : Okay opening Youtube...")
                speak("Okay opening Youtube.")
                firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                firefox.open('https://www.youtube.com/')

            if ("search" in command):
                if("google" in command):
                    print("Amadeus : What do you want to search Google?")
                    speak("What do you want to search Google?")
                    query = takecommand().lower()
                    firefox.open('https://www.google.com/search?channel=nrow5&client=firefox-b-d&q='+query)
                    print("Amadeus : searching : "+query)
                if("youtube" in command):
                    print("Amadeus : What do you want to search Youtube?")
                    speak("What do you want to search Youtube?")
                    query = takecommand().lower()
                    firefox.open('https://www.youtube.com/results?search_query='+query)
                    print("Amadeus : searching : "+query)


            if ("classroom" in command):
                if ("microprocessor" in command):
                    print("Amadeus : Okay opening Microprocessor Classroom...")
                    speak("Okay opening Microprocessor Classroom.")
                    firefox.open('https://classroom.google.com/c/NDUyOTU2ODkyMjc2')
                if ("operating" in command):
                    print("Amadeus : Okay opening Operating System Classroom...")
                    speak("Okay opening Operating System Classroom.")
                    firefox.open('https://classroom.google.com/c/NDUxNTAwMDEzODg1')

            if ("whatsapp" in command):
                print("Amadeus : Okay opening Whatsapp...")
                speak("Okay opening Whatsapp.")
                firefox.open('https://web.whatsapp.com/')

            if ("github" in command):
                print("Amadeus : Okay opening github...")
                speak("Okay opening github.")
                firefox.open('https://github.com/')

            if ("time" in command):
                wtime()

            if ("xampp" in command)or ("them" in command) or ("jain" in command) or ("ram" in command):
                print("Amadeus : Okay opening xampp...")
                speak("Okay opening Xampp.")
                os.startfile("C:\\xampp\\xampp-control.exe")

            if ("emi" in command) or ("ammy" in command) or ("ammi" in command) or ("honey" in command) or ("amy" in command):
                print("Amadeus : Yes Nilesh, please tell me how may i help you?")
                speak("Yes Nilesh, please tell me how may i help you?")


        except Exception as e:
            e= "True"        