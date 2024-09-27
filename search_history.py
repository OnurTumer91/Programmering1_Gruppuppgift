import os
from datetime import datetime

search_history = "Search_history.txt"

# Kontrollera om filen finns; om inte, skapa den
if not os.path.exists(search_history):
    with open(search_history, 'w') as s:
        pass  # Skapa en tom fil

def save_history(city, weather_data):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(search_history, 'a') as s:
            # Save city name, timestamp, and weather information in the file with consistent spacing
            s.write(f"{city}, {timestamp}, Temperature: {weather_data['temperature']}°C, Humidity: {weather_data['humidity']}%, Description: {weather_data['description']}, Wind Speed: {weather_data['wind_speed']} m/s\n")
    except Exception as e:
        print(f"Error when trying to save: {e}")



def read_history():
    history = []
    try:
        if os.path.exists(search_history):
            with open(search_history, 'r') as s:
                for line in s:
                    parts = line.strip().split(', ')
                    if len(parts) >= 6:  # using this to make sure all parts are in the file
                        # if the parts of the file is missing it will type out N/A so the program wont crash
                        city = parts[0]
                        timestamp = parts[1]
                        temperature = parts[2] if len(parts) > 2 else "N/A"
                        humidity = parts[3] if len(parts) > 3 else "N/A" 
                        description = parts[4] if len(parts) > 4 else "N/A"
                        wind_speed = parts[5] if len(parts) > 5 else "N/A"
                        # if all the data is there it will save it to the list as tuples so you can use it later
                        history.append((city, timestamp, temperature, humidity, description, wind_speed))
                    
        else:
            print('No search history found')
    except Exception as e:
        print(f"Error loading in search history: {e}")
    return history
