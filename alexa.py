import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime,timedelta
import wikipedia
import webbrowser
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hi Ram Ganesh")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk("i am listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        command = ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        command = ""
    
    return command

def run_alexa():
    command = take_command()
   # print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.now().strftime("%I:%M %p")
        print(time)
        talk("currant time is"+time)
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    
    elif ("who" in command) or ("tell me" in command) or ("what" in command):
        person=command.replace("who"or"what is" "tell me","")
        info=wikipedia.summary(person,3)
        print(info)
        talk(info)
    elif "open ipl match" in command:
        webbrowser.open("https://www.jiocinema.com/sports") 
        talk("playing.."+command)
        #controller.open_new_tab("https://www.jiocinema.com/sports")
    elif "joke" in command:
        #pyjokes.LANGUAGE ="hi-in"
        talk(pyjokes.get_jokes(language="hindi"))

    elif "message" in command:
        mymessage = command.replace("send message", "")
        time1 = datetime.now().strftime("%H:%M")  # Get current time
        pywhatkit.sendwhatmsg("+918989835159", mymessage, int(time1[2:3]), int(time1[4:5])+1)  # Send message
        print("Successfully Sent!")

    elif "are you single" in command:
        talk("i am in a releationship with Internet")
    
    else:
        talk('Please say the command again.')
if __name__ == "__main__":
    while True:
        run_alexa()