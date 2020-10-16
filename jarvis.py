import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Rohan!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Rohan!")
    else:
        speak("Good Evening Rohan!")

    speak("I am JARVIS, how may I help you?")


def takeCommand():
    # It takes audio input from mic and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Did you mean: {query}\n")
        speak(f"Did you mean {query}")

    except Exception:
        # print(e)
        print("Say that again please... ")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to,body):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    
    server.close()


if __name__ == "__main__":
    wishMe()
    
    while True:
        query=takeCommand().lower()

        #Logic for execution
        if 'wikipedia' in query:
            speak("Searching wikipedia...please wait")
            query = query.replace("wikipedia","")
            query = query.replace(" ","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        # elif 'play music' in query:
        #     music = ''
        #     songs = os.listdir(music)
        #     print(songs)
        #     os.startfile(os.path.join(music,songs[0]))
        
        elif 'the time' in query:  
              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"Sir,the time is {strTime}")
        elif 'stop' in query:
            speak("Quitting sir!!")
            break
        elif 'spotify' in query:
            path = 'C:\\Users\\ROHAN\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe'
            speak("Opening spotify app, sir...")
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("To whom should I send? sir!")
                contact = takeCommand().lower()
                to = contacts[contact]
                speak("What should I say?")
                body = takeCommand()
                sendEmail(to,body)
                speak("Email has been sent sir!!")
            except Exception as e:
                print(e)
                speak("Sorry!! could not send the email")


