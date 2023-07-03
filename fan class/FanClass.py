# Franchesca Marie U. Donadillo
# BSCPE 1-5

# Create class
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # initialize 
    def __init__(self, on = False, speed = SLOW, radius = 5, color = "blue"):
              
        # private data of speed, power, radius, and color of the fan
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # get power status
    def get_power(self):
        return self.__on
    
    # set power status
    def set_power(self, on):
        self.__on = on

    # get for speed
    def get_speed(self):
        return self.__speed
    
    # set speed
    def set_speed(self, speed):
        self.__speed = speed
                    
    # get radius
    def get_radius(self):
        return self.__radius
    
    # set radius
    def set_radius(self, radius):
        self.__radius = radius

    # get color
    def get_color(self):
        return self.__color
    
    # set color
    def set_color(self, color):
        self.__color = color