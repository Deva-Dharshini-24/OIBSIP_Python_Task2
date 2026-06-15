import requests

API_KEY = "c7399ff857273f6b69990db25771ec3c"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    temp = data["main"]["temp"]

    description = data["weather"][0]["description"]

    return f"{temp} degrees Celsius with {description}"