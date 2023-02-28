# In this file we are gonna configure some online functions

# region Imports
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
# endregion

# region Get IP
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
# endregion

# region Wikipedia Search
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
# endregion

# region Plat YouTube videos
def play_on_youtube(video):
    kit.playonyt(video)
# end region

# region Google Search

def search_on_google(query):
    kit.search(query)
# endregion

# region Send WhatsApp message
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
# endregion

# region Send Email

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
# endregion

# region Get News
NEWS_API_KEY = config("NEWS_API_KEY")

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
# endregion

# region Weather
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
# endregion
