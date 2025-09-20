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
import pyjokes
import schedule
import time
import smtplib
import random
import json

# ------------------- Text-to-Speech Setup -------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    print(f"Assistant: {audio}")
    engine.runAndWait()

# ------------------- Listen Voice Commands -------------------
def take_command(timeout=5, phrase_time_limit=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query.lower()

# ------------------- Greeting -------------------
def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your FunBot Assistant. How can I help you today?")

# ------------------- Reminder Scheduler -------------------
def set_reminder(rem_time, message):
    schedule.every().day.at(rem_time).do(lambda: speak(f"Reminder: {message}"))
    speak(f"Reminder set at {rem_time} for: {message}")

# ------------------- Email Sender -------------------
def send_email(to_address, subject, message, sender_email, sender_pass):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_pass)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, to_address, email_message)
        server.quit()
        speak("Email has been sent successfully!")
    except Exception as e:
        speak("Sorry, I am unable to send the email.")
        print(e)

# ------------------- Weather Info -------------------
def get_weather(location):
    try:
        url = f"https://www.google.com/search?q=weather+{location}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        temp = soup.find("div", class_="BNeawe").text
        speak(f"The current weather in {location} is {temp}")
    except Exception as e:
        speak("Sorry, I could not fetch the weather information.")

# ------------------- News Fetch -------------------
def get_news():
    try:
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_NEWSAPI_KEY"
        response = requests.get(url).text
        news_data = json.loads(response)
        articles = news_data['articles'][:5]
        speak("Here are the top news headlines:")
        for i, article in enumerate(articles):
            speak(f"{i+1}: {article['title']}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the news.")

# ------------------- System Commands -------------------
def system_control(command):
    if "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
    elif "sleep" in command:
        speak("Putting system to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "lock pc" in command:
        speak("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

# ------------------- Fun Features -------------------
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def tell_fact():
    facts = [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries but strawberries aren't.",
        "Humans share 50% of DNA with bananas."
    ]
    speak(random.choice(facts))

def motivational_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing.",
        "Don't let yesterday take up too much of today.",
        "It's not whether you get knocked down, it's whether you get up."
    ]
    speak(random.choice(quotes))

# ------------------- Main Logic -------------------
if __name__ == "__main__":
    wish()
    while True:
        # Run scheduled reminders
        schedule.run_pending()

        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)
        elif "open google" in query:
            speak("What should I search?")
            search = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search}")
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "weather" in query:
            speak("Tell me the location")
            loc = take_command()
            get_weather(loc)
        elif "joke" in query:
            tell_joke()
        elif "fact" in query:
            tell_fact()
        elif "quote" in query:
            motivational_quote()
        elif "reminder" in query:
            speak("Please tell me the time in HH:MM format")
            rem_time = take_command()
            speak("What should I remind you?")
            message = take_command()
            set_reminder(rem_time, message)
        elif "shutdown" in query or "restart" in query or "sleep" in query or "lock" in query:
            system_control(query)
        elif "news" in query:
            get_news()
        elif "who are you" in query:
            speak("I am your personal assistant FunBot. I can help you with tasks, jokes, news, weather, and more.")
        elif "no thanks" in query or "exit" in query or "quit" in query:
            speak("Thanks for using me. Have a great day!")
            sys.exit()
        else:
            speak("I didn't understand that. Can you please repeat?")
