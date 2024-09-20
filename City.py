#Stad Klassen
'''
Aim:
* Validation: Input city name -> validate -> pass on to API
* Error Handling: Manage missing or incorrect inputs
Todo:
[ ] Structure code

'''
#Import modules pyinputplus for input validation and re for regex control
import pyinputplus as pyip 
import re

#---------------------------:: City ::---------------------------#
#Blueprint for how input city names should be
class City:
    def __init__(self, city_name:str) -> None:       
        self.city_name = city_name

#______________________  :: Functions ::_________________________#
#Check if valid city input with pyinpusplus
    def get_city_name_input(self) -> str:

        self.city_name = pyip.inputStr(
            #Prompt
            prompt="Enter city name",
            #^Starts with, $Ends with alphabets or hyphens
            allowRegexes=[r'^[A-Za-z\s-]+$'],
            #From start to end, block 'empty' string
            blockRegexes=[r'^\s*$'],
            #Error handling
            errorPrompt="Input error, please only use letters, spaces. Try again!"
        )
        #Return and store the valid input into city_name
        return self.city_name


#---------------------------:: Test ::---------------------------#
