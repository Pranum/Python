
# Akhbaar padhke sunaao

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("sapi.spVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for today...lets begin")
    url ="http://newsapi.org/v2/top-headlines?country=in&apiKey=f5e210b55bd343c7aa76315c7bcc18b1"
    news = requests.get( url).text
    news_dict = json.loads(news)
    arts =news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("moving on to the next news")
    speak("Thankjs for Listening...")




