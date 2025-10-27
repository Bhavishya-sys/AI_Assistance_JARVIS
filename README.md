Overview

Jarvis is a Python-based voice assistant that listens to your voice commands, understands them, and performs real-world actions like:

Opening websites

Playing music

Reading the latest news

Responding with speech

It uses speech recognition, text-to-speech, web automation, and API integration to create an experience similar to virtual assistants like Alexa, Siri, or Google Assistant.

💻 Demo Preview

🎤 Speak “Jarvis” to wake it up →
🗣 Say a command like:

“Open YouTube”
“Play song_name”
“Tell me the news”

Jarvis listens, processes your request, and responds with a voice reply.

🧠 How It Works

Speech Recognition (speech_recognition)

Listens to your voice through the microphone

Converts spoken words into text commands

Triggers specific actions based on those commands

Text-to-Speech (pyttsx3)

Converts Jarvis’s responses into spoken voice output

Works offline, unlike many other TTS engines

Web Automation (webbrowser)

Opens websites like Google, YouTube, Facebook, or LinkedIn directly on voice command

News API Integration (requests)

Fetches real-time top headlines from the News API using your personal API key

Reads the first 5 news headlines aloud

Custom Music Library (musicLibrary)

A user-defined Python file (musicLibrary.py) that maps song names to YouTube or Spotify URLs

Jarvis plays any song when you say “Play [song name]”
Speech Input & Recognition
recognition = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognition.listen(source, timeout=2, phrase_time_limit=1)
word = recognition.recognize_google(audio)


sr.Recognizer() initializes the recognizer

sr.Microphone() captures voice input

recognize_google() converts audio to text

🗣 Text-to-Speech Response
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


The pyttsx3 library works offline and uses system voices

You can modify the voice, rate, and volume

🌐 Web Automation
if "open google" in c.lower():
    webbrowser.open("https://google.com")


Opens websites directly from your default browser

🎵 Music Player Integration
elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)


Fetches the song URL from musicLibrary.py and plays it

📰 News API Integration
API_KEY = "YOUR_NEWS_API_KEY"
r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
data = r.json()
for article in data['articles'][:5]:
    speak(article['title'])


Connects to NewsAPI.org

Reads out the top 5 news headlines

🔁 Main Loop
if __name__ == "_main_":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"


The assistant runs continuously, waiting for the wake word “Jarvis”

After detecting it, Jarvis becomes active and processes the next spoken command

⚙️ Setup & Installation
1. Install Required Libraries

Run this in your terminal:

pip install SpeechRecognition pyttsx3 requests


(Also ensure you have pyaudio installed for microphone input:)

pip install pyaudio

2. Set Up Music Library

Create a file named musicLibrary.py in the same folder:

music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}

3. Get News API Key

Sign up at https://newsapi.org
 and get a free API key.
Replace it in:

API_KEY = "YOUR_API_KEY_HERE"

4. Run the Program
python jarvis.py


Then just say:

Jarvis


…and start giving commands! 🎙️

🚀 Features

✅ Voice-controlled automation
✅ Opens popular websites
✅ Reads live news headlines
✅ Plays songs from your library
✅ Text-to-speech responses
✅ Customizable with your own commands

🧰 Tech Stack
Component	Library / API
Voice Recognition	speech_recognition
Text-to-Speech	pyttsx3
Web Automation	webbrowser
News Headlines	requests + NewsAPI
Music	Custom musicLibrary.py
Input Device	Microphone (via PyAudio)
💡 Concepts Used

Python Functions & Loops

Conditionals & String Matching

API Calls & JSON Parsing

Voice Input / Output Processing

Error Handling & Modularity
