################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

class City:
   def __init__(self,temperature,weather):
      self.temperature = temperature
      self.weather = weather
   @property
   def temperature(self):
      return self._temperature

   @temperature.setter
   def temperature(self, value):
      self._temperature = value

   @property
   def weather(self):
      return self._weather

   @weather.setter
   def weather(self, value):
      self._weather = value

cities = {
   "Quito" : City(22,"sunny"),
   "Sao Paulo" : City(17,"cloudy"),
   "New York" : City(14,"rainy")
   }
   
def get_city_weather(city):
   get_city = cities.get(city.title())
   if get_city:
      return f"{get_city.temperature} degrees and {get_city.weather}"
   else:
      return "City not found."

