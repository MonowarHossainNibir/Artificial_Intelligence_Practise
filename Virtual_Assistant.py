import speech_recognition as sr #pip install speechRecognition
import playsound #pip install playsound==1.2.2
from gtts import gTTS
import random
from time import ctime
import webbrowser
import os
import pyttsx3
import datetime
import pyaudio #pip install pipwin then pipwin install pyaudio

class Person:
    name = ''

    def setName(self, name):
        self.name = name

class MyVa:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    rand_num = random.randint(1, 20000000)
    audio_file = 'audio' + str(rand_num) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis_obj.name + ":" + audio_string)
    os.remove(audio_file)

r = sr.Recognizer()

# get the string and audio file
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)
        print("looking at the database")
        voiceData = ''
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak('Sorry.Could not understand you')
        except sr.RequestError:
            engine_speak('Sorry. My server is down.')

        print(">>", voiceData.lower())
        return voiceData.lower()


def respond(voiceData):
    # greeting
    if there_exists(['hey', 'hi', 'hay', 'hai', 'hello', 'hallo', 'hola', 'whats up']):
        greetings = ["hi, what are we going to do?" + person_obj.name,
                     "hi, how can i help you?" + person_obj.name,
                     "whatsup?" + person_obj.name]

        greet = greetings[random.randint(0, len(greetings) -1)]
        engine_speak(greet)

    # telling name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            engine_speak("my name is wanda")
        else:
            engine_speak("my name is wanda. whats your name?")

    # asking name
    if there_exists(["my name is", "i am "]):
        person_name = voiceData.split("is")[-1].strip()
        engine_speak(f"okhy, i will remember that {person_name}")
        person_obj.setName(person_name) #remember name is person object

    # google browsing
    if there_exists(["search for"]) and 'youtube' not in voiceData:
        search_term = voiceData.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for " + search_term + "on google")

    # youtube browsing
    if there_exists(["search youtube for"]):
        search_term = voiceData.split("for")[-1]
        url2 = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url2)
        engine_speak("Here is what I found for" + search_term + "on youtube")

    # current time
    if there_exists(["what is the time", "tell me the time", "what time is it"]):
        current_time = ctime().split(" ")[3].split(":")[0:2]
        if current_time[0] == "00":
            hours = '12'
        else:
            hours = current_time[0]
        minutes = current_time[1]
        current_time = f'{hours} {minutes}'
        engine_speak(current_time)

    # today date
    if there_exists(["what is the date today"]):
        x = datetime.datetime.now()
        current_date = x.strftime("%d")+x.strftime("%B")+x.strftime("%A")+x.strftime("%Y")
        engine_speak(current_date)

    # Current location as per google Map
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here , as per google maps")

    # terminate program
    if there_exists(["exit", "tata", "bye", "bye bye", "quit", "goodbye"]):
        engine_speak("GoodBye! See you!")
        exit()

person_obj = Person()
asis_obj = MyVa()
asis_obj.name = 'Wanda'
engine = pyttsx3.init()

voice_data = record_audio("Good Day")
print("You said:", voice_data)
respond(voice_data)

while True:
    voice_data = record_audio("Anything you wanna say?")
    print("You said:",voice_data)

    respond(voice_data)
