import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# engine.say('I am your alexa')
# engine.say('What can I do for you?')
# engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bro' in command:
                command = command.replace('bro','')
                print(command)
    except:
        pass
    return command

def run_bro():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')  # %H=hour %M=min %S=second   # I=12hr format of time and p=to get AM or PM
        talk('Current time is ' + time)

    elif 'tell me' in command:
        person = command.replace ('tell me', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry, I am AI and you cant date with an abstract')    
    
    elif 'are you single' in command:
        talk('I am in relation with your network')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Sorry, please say the correct command or command again.')

while True:
    run_bro()