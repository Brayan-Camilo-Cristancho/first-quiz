################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

recipeBookFreeze = {}
recipeBookBoil = {}
recipeBookWait = {}

def createRecipeBook(product,ingredients,temperature):
    
    try:
      if not (
      isinstance(product, str) and
      isinstance(ingredients, list) and
      all(isinstance(ingredient, str) for ingredient in ingredients) and
      isinstance(temperature, int)
      ):
          raise TypeError("Error in input data types.")
      
      if(temperature < 0):
          recipeBookFreeze[(tuple(ingredients)),temperature] = product.lower()
      elif (temperature >= 100):
          recipeBookBoil[(tuple(ingredients)),temperature] = product.lower()
      else:
          recipeBookWait[(tuple(ingredients)),temperature] = product.lower()  

    except TypeError as e:
        print(e)


createRecipeBook("pizza",["cheese", "dough", "tomato"],150)
createRecipeBook("snow",["water", "air"],-100)
createRecipeBook("gold",["lead", "mercury"],5000)
class MagicOven:
    def __init__(self):
        self.ingredients = []
        self.product = ""

    def add(self, item):
        self.ingredients.append(item)
    def freeze(self,temperature):
        self.product = recipeBookFreeze.get((tuple(self.ingredients),temperature), "Unidentified new product")
    def boil(self,temperature):
        self.product = recipeBookBoil.get((tuple(self.ingredients),temperature),"Unidentified new product")
    def wait(self,temperature):
        self.product = recipeBookWait.get((tuple(self.ingredients),temperature), "Unidentified new product")
    
    def get_output(self):
        return self.product
        
def make_oven():
  oven1 = MagicOven()
  return oven1

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze(temperature)
  elif temperature >= 100:
    oven.boil(temperature)
  else:
    oven.wait(temperature)

  return oven.get_output()
