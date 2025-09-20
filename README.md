# 🎙️ FunBot - Personal Voice Assistant

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) 
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/yourusername/FunBot) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🔹 Overview
FunBot is a **Python-based voice assistant** that helps users perform tasks hands-free using speech commands.  
It’s designed for **productivity, information, entertainment, and system control**. Think of it as your personal AI companion that listens and responds in real-time.  

---

## 🎯 Features

### 🖥 System & Productivity
- Open applications (Notepad, Command Prompt, Calculator)
- Shutdown, Restart, Sleep, Lock PC
- Set reminders
- Send emails (Gmail setup required)

### 🌐 Web & Multimedia
- Open YouTube, Google, Facebook
- Play YouTube videos or music
- Search topics on Google using voice
- Search Wikipedia and read summaries

### 🌤 Information & Knowledge
- Current time & date
- Weather updates (by city)
- News headlines (via NewsAPI)
- Fun facts, motivational quotes

### 😄 Fun & Entertainment
- Jokes using `pyjokes`
- Conversational responses (e.g., "How are you?")

---

## 🚀 How to Activate FunBot

Follow these steps to get FunBot up and running:

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/FunBot.git
cd FunBot
```
2. **Install Required Python Packages**
```bash
pip install pyttsx3 speechrecognition wikipedia pywhatkit requests beautifulsoup4 pyjokes schedule
```
3. **Run FunBot**
 Make sure your microphone is connected and working Then run:
```bash
python funbot.py
```
