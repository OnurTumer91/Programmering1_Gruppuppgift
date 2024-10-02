from City import City #-----------------Input Validering
from OpenWeatherApi import WeatherAPI #-------Väder API
from Weather_Presenter import Weather_Presenter #----All presentation
from search_history import save_history, read_history #------ Loggning



#------------------------------Main----------------------------#
if __name__ == "__main__":


#----------------------1. Validate input ----------------------#
    #Initialize classes
    city = City()#--------------------------------Input validation
    weather_api = WeatherAPI()  #------------------API calls
    presenter = Weather_Presenter(weather_api) #---Presents API data

    #validate city input from the user and store the value in city_chosen 
    city_chosen = city.city_user_input()

    if city.validate_city_name(city_chosen):

        #checks if city exists in api database
        if city.city_check_name_api():
            print(f"{city_chosen} is a valid city from our database! Fetching forecast...")

            #Present using the WeatherPresenter
            presenter.display_forecast(city_chosen)
            
            #store the forecast via the API in forecast_data
            forecast_data = weather_api.get_forecast(city_chosen)
            #save forecast in log file if it's not blank/none
            if forecast_data:  
                #stores latest search and prints it to a log
                latest_search = forecast_data[0] 
                save_history(city_chosen, latest_search)
                (print(f'saved log in root dir named "Search_History.txt"'))

        else:
            print(f"City {city_chosen} not found in OpenWeather API.")
    else:
        print(f"{city_chosen} is not a valid city name. Please try again.")

