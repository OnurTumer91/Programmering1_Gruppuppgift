from City import City #-----------------Input Validering
from OpenWeatherApi import WeatherAPI #-------Väder API
from Weather_Presenter import Weather_Presenter #----All presentation
from search_history import save_history, read_history #------ Loggning

def print_menu(): #---------------------------------Prints the menu
    print("\nWelcome to the Weather Application!")
    print("1. Check weather forecast")
    print("2. View search history")
    print("3. Exit")

def main(): #-----------------------------------------Main function
    city = City() #--------------------------------Input validation and city name handling
    weather_api = WeatherAPI()  #------------------API calls for weather data from OpenWeather
    presenter = Weather_Presenter(weather_api) #---Presents API data to user in a readable format

    while True: #------------------------------------Main loop
        print_menu()
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            city_chosen = city.city_user_input() # Get city name from user input

            if city.validate_city_name(city_chosen): # Validate city name using regex
                if city.city_check_name_api(): # Check if city exists in OpenWeather API database
                    print(f"{city_chosen} is a valid city from our database! Fetching forecast...")

                    # Present using the WeatherPresenter class and display the forecast
                    presenter.display_forecast(city_chosen)
                    
                    # Store the forecast via the API in forecast_data
                    forecast_data: list = weather_api.get_forecast(city_chosen)
                    # Save forecast in log file if it's not blank/none
                    if forecast_data:  
                        # Stores latest search and prints it to a log
                        latest_search = forecast_data[0] 
                        save_history(city_chosen, latest_search)
                        print(f'Saved log in root dir named "Search_History.txt"')
                else:
                    print(f"City {city_chosen} not found in OpenWeather API.")
            else:
                print(f"{city_chosen} is not a valid city name. Please try again.")
        
        elif choice == '2': #-------------------------------View search history
            history: list = read_history() # Read search history from file and store in history
            if history:
                print("\nSearch History:")
                for entry in history:
                    print(entry)
            else:
                print("No search history found.")
        
        elif choice == '3': #-------------------------------Exit the application
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid option. Please select a valid option (1-3).")

if __name__ == "__main__": #-----------------------------Run the main function
    main()
