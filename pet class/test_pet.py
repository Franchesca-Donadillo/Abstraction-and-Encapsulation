# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import Pet class
from pet_class import Pet

# promt user for name, type, and age of their pet
name = input("Enter the name of your pet: ")
type = input("Enter what type of animal is your pet: ")
age = input("Enter the age of your pet: ")

# initialize parameter
pet = Pet(name = str(), animal_type = str(), age = int())

# create object
your_pet = Pet(name, type, age)

# display
your_pet.set_name()
your_pet.set_animal_type()
your_pet.set_age()

