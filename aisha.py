import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import pyautogui as pg
import pywhatkit as pwk

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    '''Wishes User according to time of day '''
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    elif hour >= 16 and hour < 20:
        speak("Good Evening ")
    elif hour >= 20 and hour < 24:
        speak("Good Night")

    # Aisha written as Ayesha for better sounding by bot
    speak("This is Ayesha, your virtual assistant, Speed 1 terahertz, memory 1 zigabyte, How may I help you today?")

def input_command():
    ''' Takes input from user in audio via microphone and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said - {query} \n")

    except Exception as e:
        print("Can you please repeat ?")
        return "None"
    return query

def autonation_bot():
    speak("What do you want to know ? Say Store for Store Information or Track for Track Service Request")
    request = input_command().lower()
    if request == "store":
        speak("What is your query regarding ? say Sales for sales service, Vehicle for vehicle servicing or collision for Collision service?")
        request1 = input_command().lower()
        if request1 == "sales":
            speak("Sales regrading services are entertained between 9 am to 8 pm Monday to Friday and 10 am to 7 pm on Sundays")
            speak("For more information, Kindly book an appointment. Opening Appointment page for you")
            webbrowser.get('windows-default')
            webbrowser.open("https://www.autonation.com/dealers#/")
            speak("Now you can Book your appointment.")
        elif request1 == "vehicle":
            speak("Vehicle servicing is done  between 7 am to 7 pm Monday to Friday and 8 am to 5 pm on Sundays")
            speak("For more information, Kindly book an appointment. Opening Appointment page for you")
            webbrowser.get('windows-default')
            webbrowser.open("https://www.autonation.com/dealers#/")
            speak("Now you can Book your appointment.")
        elif request1 == "collision":
            speak("Collision related services are entertained between 8 am to 8 pm on weekdays only.")
            speak("For more information, Kindly book an appointment. Opening Appointment page for you.")
            webbrowser.get('windows-default')
            webbrowser.open("https://www.autonation.com/dealers#/")
            speak("Now you can Book your appointment.")
    elif request == "track":
        speak("Not available at the moment due to time constraints in project submission")


if __name__ == "__main__":
    running = True
    wish_me()
    while running:
        query = input_command().lower()
        #Execute tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.get('windows-default')
            webbrowser.open("https://youtube.com")
        elif "search youtube for " in query:
            speak("Searching youtube now")
            query = query.replace("Search youtube for", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("The results for your requested youtube search are here")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.get('windows-default')
            webbrowser.open("https://google.com")
        elif "google for " in query:
            speak("Googling now")
            query = query.replace("Google for", "")
            pwk.search(query)
            speak("The results for your requested google search are here")
        elif "open github" in query:
            speak("Opening GitHub")
            webbrowser.get('windows-default')
            webbrowser.open("https://github.com/")
        elif "open discord" in query:
            speak("Opening Discord")
            webbrowser.get("windows-default")
            webbrowser.open("https://discord.com")
        elif "open stackoverflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.get('windows-default')
            webbrowser.open("https://stackoverflow.com")
        elif "autonation" in query:
            autonation_bot()
        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Right now its {str_time}")
        elif "open tableau" in query:
            code_path = "C:\\Program Files\\Tableau\\Tableau Public 2021.2\\bin\\tabpublic.exe"
            os.startfile(code_path)
        elif "open vlc" in query:
            code_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(code_path)
        elif "screenshot" in query:
            ss = pg.screenshot()
            ss.save('C:\\Users\\pk20a\\Desktop\\Screenshot_1.png')
            os.startfile('C:\\Users\\pk20a\\Desktop')
            speak("Done. Took a screenshot")
        elif "bye" in query:
            speak("....Ok. I'm gonna sleep between 0's and 1's. See ya later. Goodbye")
            running = False








