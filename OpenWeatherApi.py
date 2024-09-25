import requests

class WeatherAPI:
    """
    A class to interact with the OpenWeatherMap API.
    I created this to simplify fetching weather data for different cities.
    """

    def __init__(self):
        """
        Initialize the WeatherAPI class with API key and base URLs.
        """
        # API key for OpenWeatherMap
        self.api_key: str = "d79f1ea93bd9d707f0623a1fe394953b"
        # Base URL for the current weather APID
        self.base_url: str = "http://api.openweathermap.org/data/2.5/weather"
        # Base URL for the forecast API
        self.forecast_url: str = "http://api.openweathermap.org/data/2.5/forecast"

    def get_weather(self, city: str) -> dict:
        """
        Gets weather data from any given city using OpenWeather API.
    
        Attribute: 
            city (str): The name of the city to get the weather data from.
    
        Returns:
            dict: A dictionary containing weather data, or None if there's an error.
        """
        # Constructing URL
        url: str = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
    
        # Error handling: using try-except block
        try:
            # Making API request
            response: requests.Response = requests.get(url)
        
            # Note: Debugging print, checking if response from API is 200 
            # print("Response status code:", response.status_code)

            # Checking response status
            if response.status_code == 200:
                full_data: dict = response.json()
                # Note: This converts the response data from JSON format into a Python dict
                # Note: By converting the response data to a Dict we can easly access keys in the main code

                # Extract and process the weather data
                weather_data: dict = {
                    "temperature": round(full_data["main"]["temp"], 1),  # Rounding temperature to 1 decimal place
                    "humidity": full_data["main"]["humidity"],
                    "description": full_data["weather"][0]["description"],  
                    # Note: The [0] is used because 'weather' is a list, and openweatherAPI docs says that
                    # Note: The first item is primary.
                    # Note: This has to be tested in the main application
                    "wind_speed": full_data["wind"]["speed"]
                }
                # Note: I thought about adding more attributes
                # Note: I had several attributes to choose from, "temp_min", "temp_max" "feels_like"
                # Note: I decided that 4 attributes is enough since for this assignment
                # Note: If description is prone to crashing, we will change it
                
                return weather_data
            else:
                # if request failed, print error and return None
                print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
                return None

        except:
            # Handling any unexpected errors
            print("An error occurred while trying to fetch the weather data.")
            print("Please check your internet connection and try again.")
            return None

    def get_forecast(self, city: str) -> list:
        """
        Gets a 5-day weather forecast from any given city using OpenWeather API.
        
        Attributes:
            city (str): The name of the city to get the 5 day forecast for.
        
        Returns:
            list: A list of dictionaries containing forecast data for 5 days, or None if there's an error.
        """
        # Creating URL
        url: str = f"{self.forecast_url}?q={city}&appid={self.api_key}&units=metric"
        
        # Error handling: using try-except block
        try:
            # Making API request
            response: requests.Response = requests.get(url)
            
            # Note: Debugging print
            # print("Response status code:", response.status_code)

            # Checking response status
            if response.status_code == 200:
                full_data: dict = response.json()
                # Note: This converts the response data from JSON format into a Python dict
                # Note: By converting the response data to a Dict we can easily access keys in the main code
                
                # Extract and process the forecast data
                forecast_data: list = []
                for item in full_data['list'][::8]: 
                    # Note: Get data for every 24 hours, stepping by 8 
                    # Note: The OpenWeatherAPI gives forecast data in 3 hours intervals
                    # Note: Using basic math 3 * 8 == 24 
                    
                    forecast_data.append({
                        "date": str(item['dt_txt'].split()[0]),
                        # Note: dt_txt stands for data text, it is specific to OpenWeatherAPI, not python standard syntax
                        # Note: Found in OpenWeatherAPI docs
                        # Note: split() is used to extract date. The API returns a str like "2023-09-25 12:00:00",
                        # Note: and split()[0] takes out the date "2023-09-25"

                        "temperature": float(round(item['main']['temp'], 1)), 
                        # Rounding the temperature to 1 decimal 

                        "humidity": int(item['main']['humidity']),

                        "description": str(item['weather'][0]['description']),
                        # Using index 0 as 'weather' is a list containing only one item, see earlier notes
                        "wind_speed": float(item['wind']['speed'])
                    })
                
                return forecast_data[:5]  # Return data for 5 days
            else:
                # If request failed, basic error handling
                print(f"Error: Unable to fetch forecast data. Status code: {response.status_code}")
                return None

        except:
            # Handling any unexpected errors
            print("An error occurred while trying to fetch the forecast data.")
            print("Please check your internet connection and try again.")
            return None
        