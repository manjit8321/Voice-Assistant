#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install SpeechRecognition')


# In[2]:


get_ipython().system(' pip install pyttsx3')


# In[3]:


get_ipython().system(' pip install pipwin')


# In[7]:


get_ipython().system(' pip install pywhatkit')


# In[4]:


get_ipython().system(' pipwin install pyaudio')


# In[41]:


import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import pywhatkit
import time


print(" \n\n")
print("		******Example Of Tasks I Can Perform********\n")
print("	-------------------------------------------------------")
print(" 			Windows Media Player")
print(" 			Notepad")
print(" 			Youtube")
print(" 			Chrome Browser")
print(" 			Gmail")
print(" 			LikedIn")
print(" 			Microsoft Teams")
print(" 			 WhatsApp")
print(" 			 Quit or Exit")
print("	-------------------------------------------------------\n\n")

pyttsx3.speak("Welcome")

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=5)
        pyttsx3.speak("Hello dear, I am Manjit's Assistant, How can I help you.. \n")
        pyttsx3.speak("Start saying...")
        print("Start Saying...")
        audio = r.listen(source)
        pyttsx3.speak("Okay, Please wait for a while!!....")
        print("Okay!!, Please wait for a while!!....")
        print(" ")
        
    p = r.recognize_google(audio)
    print("You said : {}". format(p))
    
    
    if("Notepad" in p) or ("Editor" in p):
        pyttsx3.speak("Opening Notepad for you")
        os.system("Notepad")
    elif("Media Player" in p):
        pyttsx3.speak("Opening Media Player for you")
        os.system("wmplayer")
    elif("Chrome" in p) or ("Browser" in p):
        pyttsx3.speak("Opening Chrome Browser for you")
        webbrowser.open("Chrome")
    elif("Gmail" in p) or ("Email" in p):
        pyttsx3.speak("Opening Mail for you")
        webbrowser.open("https://mail.google.com")
    elif("who are you" in p) or ("what is your name" in p) or ("who developed you" in p):
        pyttsx3.speak("Hi this is Manjit Roy's Assistant how can i assist you. Just ask anything.")
    elif("YouTube" in p):
        pyttsx3.speak("Opening Youtube for you")
        webbrowser.open("https://www.youtube.com/")
    elif("LinkedIn" in p):
        pyttsx3.speak("Opening LinkedIn for you")
        webbrowser.open("https://www.linkedin.com/")
    elif("WhatsApp" in p):
        pyttsx3.speak("Opening WhatsApp for you")
        webbrowser.open("https://web.whatsapp.com/")
    elif("Microsoft" in p) or ("Teams" in p):
        pyttsx3.speak("Opening Microsoft Teams for you")
        webbrowser.open("https://www.microsoft.com/en-in/microsoft-teams/log-in")
    elif("exit" in p) or ("quit" in p):
        pyttsx3.speak("Closing the Program")
        pyttsx3.speak("Thanks! For your time")
        print("Thanks! For your time.")
        
    elif('play' in p):
      #  audio = take_audio()
        song = p.replace('play', '')
        pyttsx3.speak('Playing' + song)
        pywhatkit.playonyt(song)
    
    elif('time' in p):
      #  audio = take_audio()

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
       # print(current_time)
        pyttsx3.speak(' current time is' + current_time) 
        
    elif ('how are you' in p):
        pyttsx3.speak("I am fine, Thank you")
        pyttsx3.speak("How are you, Sir")
 
    elif ('fine' in p) or ("good" in p):
        pyttsx3.speak("It's good to know that your fine")
        
    elif ('bye' in p) or ("See you" in p):
        pyttsx3.speak("Bye Take Care")
        break
    else:
        print(" Error!! ")
        pyttsx3.speak("Sorry.. Unable to hear")


# In[ ]:





# In[ ]:




