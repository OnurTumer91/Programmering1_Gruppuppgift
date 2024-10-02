import requests

class WeatherAPI:
    """
    A class to collect data from the OpenWeatherMap API.
    I Created this to get weather data from different cities.
    """

    def __init__(self):
        """
        Initialize the WeatherAPI class with API key and the two base URLs.
        """
        # API key for OpenWeatherMap
        self.api_key: str = "d79f1ea93bd9d707f0623a1fe394953b"
        # Base URL for the current weather API
        self.weather_url: str = "http://api.openweathermap.org/data/2.5/weather"
        # Base URL for the forecast API
        self.forecast_url: str = "http://api.openweathermap.org/data/2.5/forecast"

    def get_weather(self, city: str) -> dict:
        """
        Getting current weather data from a specific city
    
        Attribute: 
            city (str): The name of the city to get the weather data from.
    
        Returns:
            dict: A dictionary with temperature, humidity, description, wind speed
        """
        # Creating the entire API url by adding, city and api key and metric unit 
        url: str = f"{self.weather_url}?q={city}&appid={self.api_key}&units=metric"
    
        try:
            response: requests.Response = requests.get(url)
        
            if response.status_code == 200:
                full_data: dict = response.json()
                # Note: This converts the response from JSON format into a Python dict
                #By converting JSON to a Dict we can easly access relevant keys to extract

                # This is the data we decided to extract for our application
                weather_data: dict = {
                    "temperature": float(round(full_data["main"]["temp"], 1)),  # Rounding temperature to 1 decimal place
                    "humidity": int(full_data["main"]["humidity"]),
                    "description": str(full_data["weather"][0]["description"]),  
                    # Note: The [0] is used because 'weather' is a list, and openweatherAPI docs says that
                    #The first item is primary.
                    "wind_speed": float(full_data["wind"]["speed"])
                }
                # Note: We had several attributes to choose from, "temp_min", "temp_max" "feels_like"
                # We decided that 4 attributes is enough since for this assignment
                
                return weather_data
           
            else:
                print(f"Error: Unable to get the current weather data. Status code: {response.status_code}")
                return None

        # Here we handle both network errors and also unexpected errors.
        except requests.ConnectionError:
            print("Please check your internet connection and try again.")
            return None 
        except Exception as e: 
            print(f"An error occured in form of {e}")
            return None

    def get_forecast(self, city: str) -> list:
        """
        Gets a 5-day weather forecast from any given city that exists in OpenWeather API.
        
        Attributes:
            city (str):  Name of the city to get the forecast for.
        
        Returns:
            list: A list of dictionaries containing the forecast data, or None if there's an error.
        """
        
        url: str = f"{self.forecast_url}?q={city}&appid={self.api_key}&units=metric"
    
        try:
            response: requests.Response = requests.get(url)
            
            if response.status_code == 200:
                full_data: dict = response.json()
                       
                forecast_data: list = []
                for item in full_data['list'][::8]: 
                    # The OpenWeatherAPI gives us forecast data in 3 hours intervals
                    # We decided that this was easier for clarity, since this gives us less data points
                    # it uses step 8, so it takes first index and hops over the following 7
                    
                    forecast_data.append({
                        "date": str(item['dt_txt'].split()[0]),
                        # Note: split() is used to extract date. The API call returns a date and time, ex "2023-09-25 12:00:00",
                        # and by using  split()[0] we take out the date "2023-09-25"

                        "temperature": float(round(item['main']['temp'], 1)), 
                        # Rounding the temperature to 1 decimal 
                        "humidity": int(item['main']['humidity']),
                        "description": str(item['weather'][0]['description']),
                        "wind_speed": float(item['wind']['speed'])
                    })
                
                return forecast_data[1:]  
            else:
                print(f"Error: Unable to get the forecast data. Status code: {response.status_code}")
                return None
                
        
        except requests.ConnectionError:
            print("Please check your internet connection and try again.")
            return None
        except Exception as e: 
            print(f"An error occured in form of {e}")
            return None
        
