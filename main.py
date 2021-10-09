import speech_recognition as sr
import pyttsx3 as ptt
import pywhatkit as pw
import datetime
import wikipedia as wiki
import pyjokes as pj



listener = sr.Recognizer()
engine= ptt.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
       # print(command)
            if 'Alexa' in command:
                command=command.replace('Alexa',' ')
                talk(command)
            else:
                print('Word  is not found')
    except:
        pass
    return command

def run_alexa():

    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing'+ song)
        pw.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is'+ time)
    elif 'who' in command:
        person = command.replace('who','')
        info=wiki.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pj.get_jokes())
        talk(pj.get_jokes())

while True:
    run_alexa()


