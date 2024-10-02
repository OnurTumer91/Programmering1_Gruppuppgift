


class Weather_Presenter:
    def __init__(self, weather_api):
        self.weather_api = weather_api
#Gather and prints data from "get_weather", error message if failed
    def display_current_weather(self, city):
        weather_data = self.weather_api.get_weather(city)
        if weather_data:
            print(f"\nCurrent Weather in {city}:")
            print(f"Temperature: {weather_data['temperature']}°C")
            print(f"Humidity: {weather_data['humidity']}%")
            print(f"Description: {weather_data['description'].capitalize()}")
            print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        else:
            print(f"Unable to fetch weather data for {city}")
#Gather and displays data from "get_forecast", error message if failed
    def display_forecast(self, city):
        forecast_data = self.weather_api.get_forecast(city)
        if forecast_data:
            print(f"\n5-Day Weather Forecast for {city}:")
            for day in forecast_data:
                print(f"\nDate: {day['date']}")
                print(f"Temperature: {day['temperature']}°C")
                print(f"Humidity: {day['humidity']}%")
                print(f"Description: {day['description'].capitalize()}")
                print(f"Wind Speed: {day['wind_speed']} m/s")
        else:
            print(f"Unable to fetch forecast data for {city}")