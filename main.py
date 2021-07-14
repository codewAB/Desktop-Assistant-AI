import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import smtplib
from email.message import EmailMessage
import random
from requests import get
import pyjokes
import requests
import operator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

strTime = datetime.datetime.now().strftime("%I:%M %p")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Hello sir Good Morning its {strTime}")

    elif hour>=12 and hour<18:
        speak(f"Hello sir Good Afternoon its {strTime}")

    else:
        speak(f"Hello sir Good Evening its {strTime}")

    speak("JARVIS is here sir. tell me how may I help you")   

def takecommand():
    '''it takes microphone input form user 
    and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: , {query}\n")

    except Exception as e:
        # speak("i am sorry sir, i didnt heard that")
        return "None"
        query = query.lower
    return query

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('yourgmailid@gmail.com', 'yourpw@123')
    email = EmailMessage()
    email['From'] = 'yourgmailid@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def get_email_info():
    speak('To Whom you want to send email sir')
    name = takecommand()
    receiver = email_list[name]
    print(receiver)
    speak('What is the subject of your email sir?')
    subject = takecommand()
    speak('Tell me the text in your email sir')
    message = takecommand()
    send_email(receiver, subject, message)
    speak('Your email is sent sucessfully')
    speak('Do you want to send more emails?')
    send_more = takecommand()
    if 'yes' in send_more:
        get_email_info()
    else:
        speak('ok sir.')
        pass

email_list = {
    'sir': 'abeed.sayyed.10@gmail.com',
    'Simran': 'simrinjanemitr@gmail.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


def TasksExecution():
    wishMe()
    while True:
        query = takecommand()
        query = query.lower()

        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube..')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('what should i search on google')
            cm = takecommand()
            speak('searching on google'+ cm)
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'open gmail' in query:
            speak('opening gmail..')
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir,The time is {strTime}")

        
        elif 'open code' in query:
            speak('opening v s code..')
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing...'+ song)
            pywhatkit.playonyt(song)

        elif 'youtube' in query:
            search = query.replace('search', '')
            speak('searching on youtube '+ search)
            pywhatkit.playonyt(search)
        
        elif 'sleep' in query or 'talk to you later' in query:
            speak('okay sir have a good day. you can call me anytime')
            break

        elif 'how are you' in query:
            speak('i am absolutely fine sir, what about you?')

        elif 'fine' in query or 'am good' in query:
            speak('thats great to hear from you, god bless you sir.')

        elif 'who are you' in query:
            speak('I am Jarvis your personal assistant, how can i help you sir')

        elif 'are you single' in query:
            speak('no, sorry sir i am in a relationship with wifi')

        elif 'who created you' in query:
            speak('i was created by my father aabeed sayyed , to assist you in ur tasks')
        
        elif 'who is abid' in query:
            speak('abid is my creator, my father')

        elif 'what can you do' in query:
            speak('I can send email, make a google search , get u some information from wikipedia, play youtube videos for u, tell you the time, open various websites for you, and much more sir')

        elif 'send email' in query:
            speak('ok sir')
            get_email_info()
            send_email(receiver, subject, message)

        elif 'open notepad' in query:
            speak('opening note pad..')
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'my ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'Your IP Address is {ip}')


        elif 'close notepad' in query:
            speak('okay sir closing notepad')
            os.system('taskkill/f /im notepad.exe')


        elif 'close code' in query:
            speak('okay sir closing VS code')
            os.system('taskkill/f /im code.exe')

        
        elif 'restart the system' in query:
            os.system('shutdown /r /t S')

        elif 'shutdown the system' in query:
            os.system('shutdown /s /t S')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak('sure sir  ' + joke)

        elif 'where we are' in query or 'where am i' in query:
            speak('wait sir let me check')
            try:    
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                print(city)
                state = geo_data['state']
                print(state)
                country = geo_data['country']
                print(country)
                speak(f'sir i am not sure, but i think we are in {city} city of {state}state of {country}.')
            except Exception as e:
                speak('sorry sir due to bad network i am not able to find where we are')
                pass 

        elif 'calculate' in query or 'calculation' in query:
             r = sr.Recognizer()
             with sr.Microphone() as source:
                 speak('what you want to calculate sir ,  for example: 2 plus 2')
                 print("Listening...")
                 r.adjust_for_ambient_noise(source)
                 r.energy_threshold = 500
                 audio = r.listen(source)
             my_string = r.recognize_google(audio)
             print(my_string)
             def get_operator_fn(op):
                 return{
                     '+' : operator.add,
                     '-' : operator.sub,
                     'x' : operator.mul,
                     'divided' : operator.__truediv__,
                 }[op]
             def eval_binary_expr(op1, oper, op2):
                 op1,op2 = int(op1), int(op2)
                 return get_operator_fn(oper)(op1,op2)
             speak('your result is')
             speak(eval_binary_expr(*(my_string.split()))) 






if __name__ == "__main__":
    while True:
        ask = takecommand()
        ask = ask.lower()
        if 'wake up jarvis' in ask or 'hello ' in ask or 'hey' in ask or 'hi' in ask or 'jarvis' in ask:
            TasksExecution()
        elif 'quit' in ask or 'goodbye' in ask or 'exit' in ask or 'terminate' in ask:
            speak('goodbye sir i will miss you.')
            SystemExit()


        





























































        
