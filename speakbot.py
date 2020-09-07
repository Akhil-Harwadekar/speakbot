import pyttsx3
import datetime
import os
import random
import time
import webbrowser
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init() # object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices.

print('\t \t \t Welcome to Akhil\'s Program')
print('\t \t \t----------------------------')	

def greet():
    name="Akhil"
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        pyttsx3.speak("Good Morning "+name+". I am your virtual Assistant")
    elif hour>=12 and hour<18:
        pyttsx3.speak("Good Afternoon "+name+". I am your virtual Assistant") 
    else:
        pyttsx3.speak("Good Night"+name+". I am your virtual Assistant") 

def speak(audio):  
  engine.say(audio)
  engine.runAndWait()
  time.sleep(1)

def donot(ip):
  if(("dont" in ip) or ("do not" in ip) or ("don\'t" in ip)):
    speak("Okay...")
    exit()
  else:
    return 

def say():
  print()
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak Up..")
    audio=r.listen(source)
    try:
      text=r.recognize_google(audio)
      print("Recognizing...")
      return text
    except:
      speak("Sorry, I did not hear !")
      say()

if __name__ == "__main__":
  greet()
  print()
  print("\t ~~~ These are the most prominent tasks that I do for you ~~~")  
  print(" 1) Browser \t 2) Editors \t 3) Media Players \t 4) Date \t 5) Time \t 6) Calender \t 7) Wikipedia \t 8) Instagram \t 9) WhatsApp \t 10) Facebook")
  print("11) Youtube \t 12) Gmail \t 13) Calculator \t 14) MS-Paint \t 15) Font-Colour \t 16) Create Folder \t 17) Delete Folder \t 18) Open Folder \t 19) File Explorer \t 20) Camera")   
  print("21) Create Secured Folder \t 22) IP-configuration \t 23) Ping \t 24) Website \t 25) WiFi \t 26) Hotspot \t 27) Available Networks \t 28) Search Apps in Store \t 29) Weather \t 30) Songs")
  print("31) Set Alarm \t 32) Python \t 33) Control-Panel \t 34) Settings \t 35) Running Process \t 36) Clear Screen \t 37) LogOut \t 38) Restart \t 39) Shut-Down \t 40) Exit")
  print()
  while True:
    pyttsx3.speak("How can I help you ?")
    s=say().lower()
    print()

    if (("run" in s) or ("launch") or ("open")) and ( ("chrome" in s) or ("google" in s)):                                           #chrome
      donot(s)
      speak("Opening Google Chrome")
      os.system("chrome")

    elif (("run" in s) or ("launch") or ("open")) and ( ("edge" in s) or ("microsoft edge" in s) or ("microsoftedge" in s)):        #edge
      donot(s)  
      speak("Opening Microsoft Edge")
      os.system("microsoftedge")

    elif (("run" in s) or ("open" in s) or ("launch" in s)) and ("browser" in s):                                                   #browser
      donot(s)
      speak("Two browsers detected. Google Chrome and Microsoft Edge. Which one to open?")
      print("1. Chrome \t 2.Edge \t ", end='')
      editor=say().lower()
      if ("1" in editor) or ("chrome" in editor) or("google chrome" in editor):
        speak("Opening Google Chrome")
        os.system("chrome")
      elif ("2" in editor) or ("edge" in editor) or ("microsoft edge" in editor) or ("microsoftedge" in editor):
        speak("Opening Microsoft Edge")
        os.system("microsoftedge")
      else:
        speak("Sorry, I don't understand")
        exit()

    elif (("run" in s) or ("open" in s) or ("launch" in s)) and (("notepad" in s) or ("notepad-editor" in s) or ("file" in s)):       #notepad / any file
      donot(s)
      speak("Opening Notepad")
      os.system("notepad")

    elif (("run" in s) or ("open" in s) or ("launch" in s)) and (("wordpad" in s) or ("wordpad-editor" in s)):                      #wordpad
      donot(s)
      speak("Opening Wordpad")
      os.system("wordpad")

    elif (("run" in s) or ("open" in s) or ("launch" in s)) and (("editor" in s) or ("text" in s)):                                 #text editor
      donot(s)
      speak("Two editors detected. Notepad and Wordpad. Which one to open?")
      print("1. Notepad \t 2.Wordpad ", end='')
      editor=say().lower()
      if ("note" in editor) or("notepad" in editor):
        speak("Opening Notepad")
        os.system("notepad")
      elif ("word" in editor) or("wordpad" in editor):
        speak("Opening Wordpad")
        os.system("wordpad")
      else:
        speak("Sorry, I don't understand")
        exit()
      		
    elif (("run" in s) or ("open" in s) or ("launch" in s)) and (("windows player" in s) or ("windows  media" in s)):                       #win player
      donot(s)
      speak("Opening Windows Media Player")
      os.system("wmplayer")
 
    elif (("run" in s) or ("open" in s) or ("launch" in s)) and ("vlc" in s):                                                            #vlc
      donot(s)
      speak("Opening VLC Player")
      os.system("vlc")

    elif (("run" in s) or ("open" in s) or ("launch" in s)) and (("media" in s) or ("player" in s)):                                        #media
      donot(s)
      speak("Two media players detected. VLC and Windows Media Player. Which one to open?")
      print("1. VLC\t 2.Windows Media Player", end='')
      editor=say().lower()
      if ("vlc" in editor):
        speak("Opening VLC Player")
        os.system("vlc")
      elif ("windows" in editor) or("windows media player" in editor):
        speak("Opening Windows Media Player")
        os.system("wmplayer")
      else:
        speak("Sorry, I don't understand")
        exit()

    elif (("run" in s) or ("open" in s) or ("launch" in s)) and ("python" in s):                                                              #python 
      donot(s)
      speak("Opening Python Prompt")
      os.system("python")

    elif ("clear" in s) or ("clear sscreen" in s) :                                                                          #clear screen 
      donot(s)
      speak("Clearing the screen")
      os.system("cls")

    elif (("show" in s) or ("display" in s)) and ("date" in s):                                                                          #date
      donot(s)
      speak("Showing today's date")
      os.system("date /t")
      print("Press Enter to continue")

    elif (("set" in s) or ("keep" in s)) and ("alarm" in s):                                                                          #set alarm
      donot(s)
      speak("Set your Alarm time")
      os.system("start ms-clock:")

    elif (("show" in s) or ("display" in s)) and (("time" in s) or ("clock" in s) or ("watch" in s)):                                    #time
      donot(s)
      speak("Time is ")
      os.system("time /t")
      print("Press Enter to continue")
    
    elif (("show" in s) or ("display" in s) or ("open" in s)) and (("day" in s) or ("calender" in s)):                                    #calender
      donot(s)
      speak("Opening the calender")
      os.system("start outlookcal:") 

    elif (("change" in s) or ("apply" in s)) and (("font colour" in s) or ("colour" in s)):                              #color
      donot(s)
      speak("Which colour you would like to change your text to?")
      print("0-Black \t 1-Blue \t 2-Green \t 3-Aqua \t 4-Red")
      print("5-Purple \t 6-Yellow \t 7-White \t 8-Gray \t 9-Light Blue \t :- ",end='')
      fg=say().lower()
      if("black" in fg):
        os.system("color 0")
        speak("Colour changed to Black successfully.")
      elif("blue" in fg):
        os.system("color 1")
        speak("Colour changed to Blue successfully.")
      elif("green" in fg):
        os.system("color 2")
        speak("Colour changed to Green successfully.")
      elif("aqua" in fg):
        os.system("color 3")
        speak("Colour changed to Aqua successfully.")
      elif("red" in fg):
        os.system("color 4")
        speak("Colour changed to Red successfully.")
      elif("purple" in fg):
        os.system("color 5")
        speak("Colour changed to Purple successfully.")
      elif("yellow" in fg):
        os.system("color 6")
        speak("Colour changed to Yellow successfully.")
      elif("white" in fg):
        os.system("color 7")
        speak("Colour changed to White successfully.")
      elif("gray" in fg):
        os.system("color 8")
        speak("Colour changed to Gray successfully.")
      elif("light blue" in fg):
        os.system("color 9")
        speak("Colour changed to Light Blue successfully.")
      else:
        speak("Invalid Color")
      
    elif ("hello" in s):                                                                                                           #greet1
      speak('Hi there ! Nice to meet you')    

    elif ('how are you' in s):                                                                                                     #greet2
      stMsgs = ['I am feeling good and I\'m getting better!', 'Not too shabby at all ', 'I am Good, with full of energy','I am super cool!']     
      ans_q = random.choice(stMsgs)
      speak(ans_q)
      speak('How are you ?')
      print('How are you ? ',end='')
      resp=input().lower()
      if ("happy" in resp) or ("cool" in resp) or ("super" in resp) or ("fantastic" in resp) or ("fine" in resp)  or ("good" in resp):
        speak("Wow, that\'s great !")
      elif ("sad" in resp) or ("not" in resp) or ("upset" in resp) or ("disappoint" in resp) or ("no" in resp):
        speak("ohhh..! i'm Sorry")
      else:
        speak('Okay Good')     

    elif ('built' in s) or ('created' in s) or ('developed' in s):                                                                   #greet3
      ans_m = "master Akhil gave me a life! And I am very much greatful to him "
      speak(ans_m)
      print(ans_m)

    elif ('beautiful' in s) or ('sweet' in s) or ('good' in s):                                                                   #greet4
      ans_m = "Oh wow. You can't tell but I\'m totally blushing right now "
      speak(ans_m)
      print(ans_m)

    elif ("who are you" in s) or ("about you" in s) or ("your details" in s) or ("something" in s):                         #greet5
      about = ("I am an A I based computer program. But i can help you like you are my close friend!")
      speak(about)
      print(about+"(version 1.0)")

    elif "wikipedia" in s:                                                                                                    #wikipedia
      donot(s)
      speak("Searching Wikipedia")
      s=s.replace("wikipedia","")
      results = wikipedia.summary(s,sentences=1)
      speak(results)
      speak("Thats all in brief")

    elif (("open" in s) or ("launch" in s)) and (('instagram' in s) or ("insta" in s)):                                            #instagram
      donot(s)
      speak("opening Insta gram")
      webbrowser.open("https://www.instagram.com")

    elif (("open" in s) or ("launch" in s)) and ('facebook' in s) or ("fb" in s):                                                  #facebook
      donot(s)
      speak("opening facebook")
      webbrowser.open("https://www.facebook.com")

    elif (("open" in s) or ("launch" in s)) and ('youtube' in s):                                                                  #youtube
      donot(s)
      speak("opening youtube")
      webbrowser.open("https://www.youtube.com")

    elif (("open" in s) or ("launch" in s)) and ('whatsapp' in s):                                                                   #whatsapp
      donot(s)
      speak("opening whatsapp")
      webbrowser.open("https://www.whatsapp.com")

    elif (("open" in s) or ("launch" in s)) and (('mail' in s) or ("gmail" in s) or ("email" in s)):                                 #gmail
      donot(s)
      speak("opening G mail")
      webbrowser.open("https://www.gmail.com")

    elif (("tell" in s) or ("show" in s)) and (('weather' in s) or ("climate" in s) or ("temperature" in s)):                                 #weather
      donot(s)
      speak("Opening M S N weather")
      os.system("start bingweather:")

    elif (("open" in s) or ("launch" in s)) and (('run' in s) or ("website" in s) or ("link" in s) or ("webpage" in s)):           #open any website
      donot(s)
      speak("Provide me the U R L of the page you wish to open")
      print("Type the URL here :- ",end='')
      link=input()
      os.system("start "+link)

    elif (("show" in s) or ("launch" in s) or ("open" in s)) and (('control panel' in s) or ("control-panel" in s)):               #control panel
      donot(s)
      speak("opening Control Panel")
      os.system("control panel")

    elif (("show" in s) or ("display" in s) or ("open" in s)) and (('processes' in s) or ("programs" in s)):               #show current running process
      donot(s)
      speak("Showing all the present running tasks")
      os.system("tasklist")

    elif (("launch" in s) or ("open" in s)) and (('paint' in s) or ("ms" in s) or ("drawing board" in s) ):                  #MS paint
      donot(s)
      speak("opening Microsoft Paint")
      os.system("mspaint")

    elif (("show" in s) or ("open" in s)) and (('ipconfig' in s) or ("ip" in s) or ("ipaddress" in s)):                  #ipconfig
      donot(s)
      speak("opening IP Configuration")
      os.system("ipconfig")

    elif (("connect" in s) or ("check" in s) or ("ping" in s)) and (('server' in s) or ("ip" in s) or ("connectivity" in s)):                 #ping
      donot(s)
      speak("Provide the I P Address to ping")
      print("IP Address to ping :- ",end='')
      ipadd=input()
      speak("Pinging to "+ipadd)
      os.system("ping "+ipadd)

    elif (("launch" in s) or ("open" in s)) and (('camera' in s) or ("cam" in s)):                                                #camera
      donot(s)
      speak("opening Camera")
      os.system("start microsoft.windows.camera:")

    elif ("launch" in s) and (('calci' in s) or ("calculator" in s)):                                                         #calculator
      donot(s)
      speak("opening calculator")
      os.system("calc")

    elif (("launch" in s) or ("open" in s)) and (("file explorer" in s) or  ("explorer" in s)):                               #file explorere
      donot(s)
      speak("opening File Explorer")
      os.system("explorer")

    elif (("create" in s) or ("make" in s)) and (('folder' in s) or ("directory" in s)):                                        #new secured/normal folder
      donot(s)
      speak("Provide path to create the folder")
      print("Provide path to create the folder :- ", end='')
      drive=input()
      fld=drive.replace('\\','/')
      speak("Do you want to create a secured folder ? say yes or no.")
      print("Create a secured folder ? (y/n) :",end='')
      yn=say().lower()
      if yn=="yes" or yn=="yeah":
        speak("Provide name to the folder")
        print("Provide name to the folder :- ", end='')
        name=say()
        os.system("md "+name)
        speak("New secured folder created successfully")
      elif yn=="no" or yn=="nope":
        speak("Provide name to the folder")
        print("Provide name to the folder :- ", end='')
        name=say()
        os.system("mkdir "+name)
        speak("New folder created successfully")
      else:
        speak("Folder not created")

    elif (("open" in s) or ("show" in s) or ("goto" in s) or ("location" in s)) and (('folder' in s) or ("directory" in s)):       #open folder
      donot(s)
      speak("Provide Folder path to open")
      print("Provide Folder path to open :- ", end='')
      drive=input()
      speak("You are in "+drive+" Folder now")
      os.system("start "+drive)

    elif (("delete" in s) or ("remove" in s)) and (('folder' in s) or ("directory" in s)):                                #delete folder
      donot(s)
      speak("Provide path previous to that folder")
      print("Provide path previous to that folder you wish to delete :- ", end='')
      dele=input()
      speak("Enter the folder name to delete")
      print("Enter the folder name to delete",end='')
      fldr=input()
      os.system("rd /s /q "+'"'+dele+"\\"+fldr+'"')
      speak("Folder deleted successfully.")

    elif (("connect" in s) or ("launch" in s) or ("open" in s)) and (('wifi' in s)):                                       #wifi
      donot(s)
      speak("Showing you the lists of network profiles. Please select the device")
      wifiProfile=os.system("netsh wlan show profiles")  
      print(wifiProfile)
      print("Please select the device :- ", end='')
      select=input()
      os.system("netsh wlan connect name="+'"'+select+'"')

    elif (("show" in s) or ("display" in s)) and (('available' in s) or ("networks" in s)):                                    #available networks
      donot(s)
      speak("Showing all the available networks")
      os.system("start ms-availablenetworks:")

    elif (("turnon" in s) or ("switchon" in s) or ("open" in s)) and (('hotspot' in s)):                                   #hotspot
      donot(s)
      speak("Provide Hotspot name and Password")
      print("Provide hotspot name :- ",end='')
      htname=input()
      print("Provide hotspot password :- ",end='')
      htpswd=input()
      os.system("netsh wlan set hostednetwork mode=allow ssid="+htname+"key="+htpswd)
      os.system("wlan start hostednetwork")

    elif (("play" in s) or ('sing' in s)) and (("music" in s) or ("song" in s)):                                                  #songs
      donot(s)
      speak("Hmm!  Well,  Ok")
      music_dir = 'C:/Users/Akhil/OneDrive/Desktop/Assistant'
      musics = os.listdir(music_dir)
      randsong = random.randrange(5)
      os.startfile(os.path.join(music_dir,musics[randsong]))  

    elif (("show" in s) or ("display" in s) or ("launch" in s)) and  (("information" in s) or ("system info" in s) or ("about system" in s)):  #system info
      donot(s)
      speak("Showing System information")
      os.system("systeminfo")

    elif (("open" in s) or ("show" in s)) and  (("settings" in s) or ("system" in s)):                                      #settings
      donot(s)
      speak("Opening System settings")
      os.system("start ms-settings:")

    elif (("search" in s) or ("check" in s)) and  (("app" in s) or ("application" in s)):                                      #search apk in MS store
      donot(s)
      speak("Provide the name of the Application")
      print("Name of the application to be searched :- ",end='')
      app=input()
      os.system("start ms-"+app+":")

    elif (("exit" in s) or ("close" in s) or ("stop" in s) or ("quit" in s)  or ("abort" in s)  or ("bye" in s)):                #exit
      donot(s)
      speak("Well, I'm going. Bye")
      break

    elif (("shutdown" in s) or ("turnoff" in s)) and  (("pc" in s) or ("computer" in s) or ("system" in s)):                    #shutdown
      donot(s)
      speak("Shutting Down.")
      os.system("shutdown -s")

    elif (("restart" in s) or ("reopen" in s)) and  (("pc" in s) or ("computer" in s) or ("system" in s)):                    #restart
      donot(s)
      speak("Restarting your system.")
      os.system("shutdown -r")

    elif (("logout" in s) or ("signout" in s)) and  (("pc" in s) or ("computer" in s) or ("system" in s)):                    #logout
      donot(s)
      speak("Shutting Down.")
      os.system("shutdown -l")

    else:
      temp = s.replace(' ','+')                                                                                                       #google search
      geturl="https://www.google.com/search?q="    
      res_g = 'Sorry! I did not understand, but I will take you to internet to give you the best possible answer !'
      print(res_g)
      speak(res_g)
      webbrowser.open(geturl+temp) 
