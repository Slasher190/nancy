import speech_recognition as sr
from pywinauto.application import Application
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommandHindi(): 
         
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
          
        # seconds of non-speaking audio before  
        # a phrase is considered complete 
        print('Listening') 
        r.pause_threshold = 0.7  
        audio = r.listen(source)   
        try: 
            print("Recognizing") 
            Query = r.recognize_google(audio, language='hi-In') 
              
            # for listening the command in indian english 
            print("the query is printed='", Query, "'") 
          
        # handling the exception, so that assistant can  
        # ask for telling again the command 
        except Exception as e: 
            print(e)   
            print("Say that again sir") 
            return "None"
        return Query 
  
  takeCommandHindi() 
  
# Driver Code 
           
# call the function 
 
def ask():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something ...")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Nancy Sir. Please tell me how may I help you")

def stickNote():
    # data = ask().lower()
    print("Openenig Notepad ...")
    speak("Opening Notepad ...")
    app = Application(backend="uia").start("notepad.exe")
    app
    new_data = ask().lower()
    time.sleep(2)
    if "type" in new_data:
        # dat1 = ""
        speak("Give me information to type")
        print("Give me information to type")
        new_data1 = ask()
        
        app.UntitledNotepad.type_keys(new_data1)
        # if (new_data1 == "double stop"):
        #     app.
        # app.UntitledNotepad.menu_select("File->SaveAs")
        # app.SaveAs.ComboBox5.select("UTF-8")
        # app.SaveAs.edit1.set_text("Example-utf8.txt")
        # app.SaveAs.Save.click()

            

if __name__=="__main__":
    wishMe()
    while(True):
        data = ask().lower()
        if "make notes" in data:
            stickNote()
      
