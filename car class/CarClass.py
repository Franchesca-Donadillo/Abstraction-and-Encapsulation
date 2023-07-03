# Franchesca Marie U. Donadillo
# BSCPE 1-5

# create car class
class Car:
    # initialize method
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # get speed
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed
        
    # accelerate method that adds 5 from the speed data
    # break method that subtracts 5 from the speed data
    # get_speed method to return current speed
