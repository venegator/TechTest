import requests
import os

# Taking the values from OWM_CITY and OWM_API_KEY environment variables.
cityName = os.getenv('OWM_CITY')
apiKey = os.getenv('OWM_API_KEY')

urlGoecodingAPI = "http://api.openweathermap.org/geo/1.0/direct?q=" + cityName + "&limit=1&appid=" + apiKey

r = requests.get(urlGoecodingAPI) #First request to get geolocation values (latitude, longitude) using OpenWeatherMap GeoCoding API.

if r.status_code == 200 and r.text != "[]":
    cityData = r.json()
    cityLatitude = cityData[0]['lat']
    cityLongitude = cityData[0]['lon']

    urlCurrentWeatherAPI = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(cityLatitude) + "&lon=" + str(cityLongitude) + "&units=metric&appid=" + apiKey

    r2 = requests.get(urlCurrentWeatherAPI) # Second request to get the weather information using OpenWeatherMap CurrentWeatherData API.

    currentWeather = r2.json()
    description = currentWeather['weather'][0]['description']
    temperature = currentWeather['main']['temp']
    humidity = currentWeather['main']['humidity']

    print("Hi! The current weather in %s is %s, with a temperature of %d celsius and %d percent of humidity." % (cityName, description, temperature, humidity))
else:
    print("The location introduced is not correct or not present in the database. Please try another one.")