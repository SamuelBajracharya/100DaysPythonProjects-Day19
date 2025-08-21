import requests

_API_KEY = "de9293f7d4ce2922348e0db8cc2061b6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={_API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}C",
                "Weather": data["weather"][0]["description"].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']}m/s",
            }
            return weather
        elif response.status_code == 404:
            print("City not found.")
        else:
            print("An error occurred. Status Code: ", response.status_code)
    except Exception as e:
        print("An error occurred: ", e)
    return None


def display_weather(weather):
    print("\n---Weather Information---")
    for key, value in weather.items():
        print(f"{key}: {value}")
