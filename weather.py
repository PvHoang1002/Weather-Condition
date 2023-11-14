from pprint import pprint
import requests
import os

def get_current_weather(city="Ha Noi"):
    api_key = os.getenv("API_KEY")

    # If running on local machine, try to load API key from .env file
    if api_key is None and os.path.exists(".env"):
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("API_KEY")

    if api_key is None:
        raise ValueError("API_KEY not found in environment variables or .env file")

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
