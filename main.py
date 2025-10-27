import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognition = sr.Recognizer()                                        #initiate krne k liye
engine = pyttsx3.init()
API_KEY = "9c44523038314d63bcc5376c4ec90b61"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 

    elif "news" in c.lower() or "tell me the news" in c.lower():
     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
    if r.status_code == 200:    
        data = r.json()
        articles = data.get('articles', [])
        for article in articles[:5]:  # first 5 headlines
            title = article.get('title')
            if title:
                # print(title)
                speak(title)
    else:
        speak("Sorry, I could not fetch the news.")



if __name__ == "_main_":
    speak("Initializing jarvis....")
    while True:
        #Listen for the waKE word "jarvis"
        #obtain audio rom the microphone
        r = sr.Recognizer()
       
        print("recognizing.....")


        # recognize speech using spinx
        try:
            with sr.Microphone() as source:
               print("Listening....")
               audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if (word.lower()== "jarvis"):
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

                #listen for command
            
        except Exception as e :
            print("Error; {0}" .format(e))