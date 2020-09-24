from time import sleep
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import urllib.request
import re
import speech_recognition as sr
import pyaudio as pa

r = sr.Recognizer()
#recording function
def record():
    with sr.Microphone() as source:
    
    
     r.adjust_for_ambient_noise(source)    
     r.energy_threshold
     audio = r.listen(source)
    
     voice =""
     try:
        voice = r.recognize_google(audio)
        
                
     
     except sr.WaitTimeoutError:
        print("Are you there")
        speak("Are you there")
        
     except sr.UnknownValueError:
         
         if voice=="":
             voice=record()
   
     except sr.RequestError:
        print("i can't help you for now")   
     return voice

#Response function can be edited dynamically, its up to you.
#You can change the answers and questions.
def response(voice):
    if voice == "hi":
        print("Hi!")    
        speak("Hi")  
    elif "hello" in voice:
        print("Hello!")    
        speak("Hello")
    elif "weather" in voice:
        browser = webdriver.Chrome()  
        browser.implicitly_wait(3)
        print("I can find it with google for you")    
        speak("I can find it with google for you") 
        browser.get("https://www.google.com/search?q="+"weather")
        voice= record()
        if "quit" or "close" in voice:
            browser.close()
    #Instagram informations, need to fill the username and password        
    elif "Instagram" in voice:  
        username =""   # fill here with your username
        password =""   # fill here with your password
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)

        browser.get('https://www.instagram.com/')

    
        sleep(3)

        #instagram informations
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
      
        command =""
        browser.get("https://www.instagram.com/")
        while 1:  
            command = record()   
            print(command)
            if "profile" in command:
                browser.get("https://www.instagram.com/"+username)
                
            elif "main" or "menu" in command:
                browser.get("https://www.instagram.com/")
                sleep(1)

            elif "direct" or "messages" or "message" or "inbox" in command:
                print("inbox!")
                browser.get("https://www.instagram.com/direct/inbox/")  
                sleep(1)

            elif "exit" or "quit" or "close" in command:
                browser.close() 
                break 
    elif "how are you" in voice:
        print("i'm fine,thanks and you?")    
        speak("i'm fine,thanks and you?")
    elif " you love me" in voice:
        print("Yes i love you!!")    
        speak("Yes i love you!!")   

    #Search on Browser     
    elif "search" in voice:
     
        print("what do you want to search?")
        speak("what do you want to search?")
        url = record()
        print(url)
        browser = webdriver.Chrome()  
        browser.implicitly_wait(3)
        browser.get("https://www.google.com/search?q="+url)
        sleep(2)
        
     
        

    elif "bye" in voice:
        print("see you too")
        speak("see you too")    
        exit() 
    elif voice=="":
        print("I didn't understand")

#Function for assistant to talk it creates an audio file and delete it automatically
def speak(string):
    
    tts = gTTS(string)
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


print("how can i help you")    
speak("how can i help you")  


while 1:
  
   voice = record()
 


   print("Me : " + voice)
   response(voice)
  


    

#print(cite)
#print(browser.find_elements_by_tag_name("cite"))
#print(soup.find("cite"))
#cite = browser.find_elements_by_tag_name("cite")
#cite[len(cite)- (len(cite)-((2*n)-2))].click()
