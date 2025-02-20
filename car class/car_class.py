# Franchesca Marie U. Donadillo
# BSCPE 1-5

from termcolor import cprint, colored

# create car class
class Car:
    # initialize method
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # accelerate method that adds 5 from the speed data
    def accelerate(self):
        self.__speed += 5
        return self.__speed

    # break method that subtracts 5 from the speed data
    def break_met(self):
        self.__speed -= 5
        return self.__speed
    
    # get_speed method to return current speed
    def get_speed(self):
        return self.__speed
    
    #set speed
    def set_speed(self):
        cprint(colored("CAR'S CURRENT SPEED: " + str(self.__speed)), "blue", attrs=["bold"]) 
