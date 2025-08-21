from weather_app import get_weather, display_weather


def main():
    while True:
        print("\n---Weather App---")
        city = input("Enter a city name (or 'q' to quit): ").strip()
        if city.lower() == "q":
            break
        weather = get_weather(city)
        if weather:
            display_weather(weather)


if __name__ == "__main__":
    main()
