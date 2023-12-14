from dotenv import load_dotenv
from pprint import pprint
import requests
import os

#this will call what we have in .env file my api key
load_dotenv()

def get_current_weather(city="Aydın"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"
    
    # we try to check if we get correct url to send to website
    #print(request_url)
    
    weather_data= requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n***Get Weather Conditions\n")
    
    city = input("Please enter a city name:")
    
    # check for empty stirings and atrings with only spaces, even there is output is predefined city
    if not bool(city.strip()):
        city ="erzincan"
    
    
    weather_data = get_current_weather(city)
    
    print("\n")
    pprint(weather_data)
    
    
