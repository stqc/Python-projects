import pyttsx3
import wolframalpha
import sys
import wikipedia
import speech_recognition as sr

#assigning a client id from wolframalpha
client=wolframalpha.Client('your_client_id')

en_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

#initialising text to speech enginge
engine=pyttsx3.init()
engine.setProperty('voice', en_id)
#text to speach speed of the speech
engine.setProperty("rate", 150)
engine.say("Hello ! My name is LaD and I am the Local Assistant for your Desktop, how can I help you today?")
print("Hello ! My name is L.A.D and I am the Local Assistant for your Desktop, how can I help you today?")
engine.runAndWait()

#audio output of LAD
def reply(sen):
    engine.say(sen)
    print("LAD:"+sen)
    engine.runAndWait()

#wolfram search 
def wolf(q):
    res=client.query(q)
    return next(res.results).text

#wikipedia search
def wiki(q):
    return wikipedia.summary(q,sentences=2)

#voice input ussing SpeechRecognition
def say_somthn():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening:")
        audio = r.listen(source)
    inp=''
    try:
        inp=r.recognize_google(audio)
    except sr.UnknownValueError:
        reply("could not understand what you said try typing")
        inp=input(":")
    return inp

def lad(data):
    if 'hello' in data:
        reply("hello there!")
    elif 'hi' in data:
        reply("hello there!")
    elif 'how are you'  in data:
        reply("I am doing great and ready to serve you!")
    elif 'how\'s it going'  in data:
        reply("I am doing great and ready to serve you!")
    elif 'bye' in data:
        reply("I hope I was a good help")
        sys.exit()
    elif 'your name' in data:
        reply("I am LAD")
    elif 'what can you do' in data:
        reply("I am in a very early stage of my life but I will try my best to help you")
    elif 'who made you' in data:
        reply("Prateek Dang is my creator")
    else:
        try:
            reply("searching")
            r=wolf(data)
            reply("got it")
            reply(r)
        except:
            reply("still searching")
            r=wiki(data)
            reply("got it,")
            reply(r)

while True:
    data= say_somthn()
    data=data.lower()
    lad(data)
    
