#Stad Klassen
'''
Aim:
* Validation: Input city name -> validate -> Check with database
* Error Handling: Manage missing or incorrect inputs
* Using external data: Json or API to verify real life cities existence
Todo:
[X] Structure code
[X] Implement city_user_input
[X] Implement validate characters
[X] Make validation with real life cities using Json or API
[ ] Fix å,ä,ö et cetera
[X] Check why self.city_name is giving underlines
[X] Check why city_chosen.city_name is giving underlines
'''
#Import modules pyinputplus for input validation and re for regex control
import pyinputplus as pyip
import regex as re
import requests

#"OpenWeatherMap" API KEY
API_KEY = "d79f1ea93bd9d707f0623a1fe394953b"
#---------------------------:: City ::---------------------------#
#Blueprint for how input city names should be. 'None' will later be loaded into from the input
class City:
    def __init__(self) -> None:
        self.city_name = None
        
#_____________________  :: 1.USER INPUT ::________________________#
#Get user input using the pyinputplus String input function and store it inside city_name
    def city_user_input(self) -> str:
        self.city_name = pyip.inputStr(
            prompt="Enter city name:",
        )
        return self.city_name

#______________________  :: 2.REGEX CHECK ::_______________________#
#Validation of the input by comparing letters and spaces by using regex
    def validate_city_name(self, city_name: str) -> bool:
# \p{L} Letter from any language including ö,ö,å
# \p{M} includes tildes and accents such as ' and ´ `
# Space is allowed between words such as 'New York' or 'New-York'
        if re.match(r"^[\p{L}\p{M}]+(?:[\s'-][\p{L}\p{M}]+)*$", city_name):
            return True
        return False
    
#______:: 3.CHECK WITH OPENWEATHER API IF 'CITY' EXISTS ::__________#
    def city_check_name_api(self) -> bool:
#API Calls from https://openweathermap.org/current#name
#Fills in user input text and checks online if there is any matches
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={API_KEY}"
#Setting up try and except for error handling        
        try:
#Makes a request call
            response = requests.get(api_url)
#If the request gives back 200(Success), print
            if response.status_code == 200:
                # Print for testing purposes
                # print(f"{self.city_name} is a valid city mathcing our database.")
                return True
            else:
                # Print for testing purposes
                # print(f"City '{self.city_name}' not found in the Cities database. Try again")
                return False
#Error handling
        except requests.exceptions.RequestException as failed_connection:
            print(f"Error connecting to OpenWeather API: {failed_connection}")
            return False

#####################################TEST - DISABLE THIS PART###################################
if __name__ == "__main__":

#Initiate
    city_chosen = City()
#Retrieve city input from user
    city_chosen.city_user_input()

#1.Validate via regex
    if city_chosen.validate_city_name(city_chosen.city_name):
#2.Check if it gives online matches with real cities
        if city_chosen.city_check_name_api():
            print(f"'{city_chosen.city_name}' is a valid city according to the OpenWeather API.")
        else:
            print(f"'{city_chosen.city_name}' is not found in the OpenWeather API.")
    else:
        print(f"'{city_chosen.city_name}' is not in a valid format. No numerals or spaces please")
#####################################::TEST::#################################################
