import requests
import dotenv
import datetime as dt

# with open("api_key.txt", "r") as f:
#     API_KEY = f.read().strip()

dotenv.load_dotenv()
import os
API_KEY = os.getenv("weather_api")

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit
Base_URL = "https://api.openweathermap.org/data/2.5/weather?"

city = input("Enter the city name: ").capitalize()
url = Base_URL + "appid=" + API_KEY + "&q=" + city

response = requests.get(url)
if response.status_code == 200:
    print("API request successful.")
elif response.status_code == 401:
    print("Invalid API key. Please check your API key and try again.")
elif response.status_code == 404:
    print("City not found. Please check the city name and try again.")

# data = response.json()
# print(data)

# temp_kelvin = data['main']['temp']
# temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
# feels_like = data['main']['feels_like']
# feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like)
# humidity = data['main']['humidity']
# sunrise = dt.datetime.fromtimestamp(data['sys']['sunrise']+ data['timezone'])
# sunset = dt.datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'])
# description = data['weather'][0]['description']


# print("============ Weather Report ============")
# print(f"Weather in {city}:")
# print(f"Temperature in {city}: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F")
# print(f"Feels_like: {feels_like_celsius:.2f}°C / {feels_like_fahrenheit:.2f}°F")
# print(f"Humidity: {humidity}%")
# print(f"Sunrise: {sunrise}")
# print(f"Sunset: {sunset}")
# print(f"Weather description: {description.capitalize()}")
# print("========================================")
