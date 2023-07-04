# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import Pet class
from pet_class import Pet
import pyfiglet
from termcolor import colored, cprint

# promt user for name, type, and age of their pet
print("\n" + "INPUT".center(40))
name = input("Enter the name of your pet: ").upper()
type = input("Enter what type of animal is your pet: ").upper()
age = input("Enter the age of your pet: ").upper()

# initialize parameter
pet = Pet(name = str(), animal_type = str(), age = int())

# create object
your_pet = Pet(name, type, age)

# display
print("\n")
cprint(colored("="*40),"cyan")
print("PET INFORMATION".center(40))
your_pet.set_name()
your_pet.set_animal_type()
your_pet.set_age()
cprint(colored("="*40), "cyan")

