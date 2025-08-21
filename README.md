# Weather App 🌤️

A simple **Python-based Weather App** that fetches real-time weather information for any city using the **OpenWeatherMap API**.  

---

## Features

- Fetches current weather data for any city.
- Displays:
  - Temperature (in Celsius)
  - Weather description
  - Humidity
  - Wind speed
- Handles invalid city names gracefully.
- Interactive command-line interface.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

2. **Install dependencies** (requires Python 3.x):

```bash
pip install requests
```

3. **Get your OpenWeatherMap API Key**:  
Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get a free API key.

4. **Add your API key** in `weather_app.py`:

```python
_API_KEY = "YOUR_API_KEY_HERE"
```

---

## Usage

Run the app:

```bash
python weather_app.py
```

- Enter the city name when prompted.
- Type `q` to quit the app.


## Dependencies

- [requests](https://pypi.org/project/requests/) - For making API calls.

---

## Contributing

Feel free to submit issues or pull requests for improvements.  

---

## License

This project is licensed under the MIT License.
