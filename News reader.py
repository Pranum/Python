
# Akhbaar padhke sunaao

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("sapi.spVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for today...lets begin")
    url ="Enter your news API key"
    news = requests.get( url).text
    news_dict = json.loads(news)
    arts =news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("moving on to the next news")
    speak("Thanks for Listening...")




