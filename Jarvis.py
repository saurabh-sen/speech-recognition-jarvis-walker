import datetime
import os
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()


def speak(audio):
    """
    this function is used to speak using SAPI 5
    :param audio:
    :return: speaks output as string
    """
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """
    this function wishes the user Good Morning or Good night etc
    by using datetime module
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Walker, my clock speed is 1.6 Giga hertz to 3.4 giga hertz, memory one tera bytes, "
          "my owner is a big fan of Alan walker. Please tell me how may I help you")


def take_command():
    """
    it takes input using microphone
    :return: output as
    """

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.... Please wait ")
        query1 = r.recognize_google(audio)
        print(f"you said : {query1}")

    except Exception as e:
        # print(e)
        print("Say That again Please....")
        return "None"


if __name__ == '__main__':
    wishme()
    while True:
        query = take_command().lower()
        # Logic for executing tasks passed on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'play music' in query:
            music_directory = 'D:\\song'
            songs = os.listdir(music_directory)
            random_song = random.randint(0, (len(songs) - 1))
            os.startfile(os.path.join(music_directory, songs[random_song]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open vscode' or 'open visual studio code' in query:
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'open pycharm' in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.3\\bin\\pycharm64.exe"
            os.startfile(code_path)
        elif 'quit' in query:
            exit()
# , language='en-in'
