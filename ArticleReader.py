import pyttsx3
import requests
from bs4 import BeautifulSoup
import re
import os
from launcher import *

# Selects the speech synthesizer/driver
def TTS_driver():
    import platform
    speech = {'Windows':'sapi5', 'Linux':'espeak', 'Darwin':'nsss'}
    return speech[platform.system()]

# Initialising the speech engine
def generate_voice(speaker, speaking_rate):
    engine = pyttsx3.init(TTS_driver())
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[speaker].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate*speaking_rate)
    return engine
    
# Converts text file to speech
def speak_text_file(path, engine):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
        speak(text, engine)
        file.close()     

# Scrapes the text from the passed URL and saves the file to 'Downloads' folder(if chosen)
def speak_web_file(url, save_to_file, engine):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    paragraphs = []
    for para in soup.select('p'):
        paragraphs.append(para.getText().strip())
    article = " ".join(paragraphs)

    if save_to_file:
        title = soup.select('title')[0].getText().strip()  #''.join([para.getText().strip() for para in soup.select('title')])
        name = re.findall(r'[^!@_!#$%^&*()-<>?/\|}{~:\s]+',title)
        filename=''.join(name)
        path = os.path.join(os.environ['USERPROFILE'],'Downloads',filename+'.txt')
        file = open(path, 'w+', encoding="utf-8")
        file.write(article)
        file.close()
    speak(article, engine)

# Converts the text into speech and saves it in a .mp3 file
# Launches a browser for playing the audio file
def speak(text, engine):
    # engine.say(text)
    engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()
    launch()



# NOT IMPORTANT AS THIS FILE IS NOT MEANT TO BE ACCESSED DIRECTLY
if __name__ == "__main__": 
    url = str(input("Enter the URL: "))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    file = open('test.txt','w', encoding="utf-8")
    for para in soup.select('p'):
        file.write(para.getText().strip())
    file.close()