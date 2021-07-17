import sys

import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import pywhatkit
import requests
from bs4 import BeautifulSoup
import sys
import pyjokes
#import youtube_websearch
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voice',voice[1].id)

#text to spech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..........")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognize.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("say that again please.........")
        return "none"
    return query

#to wish
def wish():
    hour = (datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
         speak("good afternoon")
    else:
        speak("good evening")
    speak("I am fun bots how can i help you")


if __name__=="__main__":
    wish()
    while True:
        if 1:
            query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath ="C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")

            #wikipedia
        elif "wikipedia" in query:
            speak("searching wikipedia.......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        #open youtube
        elif "youtube" in query:
            webbrowser.open("www.youtube.com")

        #open google
        elif "open google" in query:
            speak("sir , what should I search on Google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        #open facebook
        elif "facebook" in query:
            webbrowser.open("www.facebook.com")


        #To send Whatsapp message
        #elif "send message" in query

        #play youtube song

        elif "play" in query:
            song = query.replace("play","")
            speak("playing" +song)
            pywhatkit.playonyt(song)

        #date and time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("current time is " + time)

        #fun comment
        elif"how are you doing now" in query:
            speak("enjoying in bed")

        elif"who are you" in query:
            speak("i am your personal assistant....How can I help you? ")
        #jokes
        elif "joke" in query:
            speak(pyjokes.get_joke())

        #send email
       # elif "send email" in query:
        #    speak("please tell me the person name")
         #   cd = takecommand().lower()
        #weather update
        elif "weather" in query:
            speak("tell me the location")
            cm = takecommand().lower()
            print (cm)

            #search = ""
            url =f"https://www.google.com/search?q='weather of ' + {cm}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="vk_bk TylWce").style
            speak(f"current {cm} is {temp}")

        elif "no thanks" in query:
            speak("Thanks for using me , have a good day")
            sys.exit()

        speak("sir , Do you have any other work")
        print("hlw")