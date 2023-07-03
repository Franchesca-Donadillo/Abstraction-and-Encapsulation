# Franchesca Marie U. Donadillo
# BSCPE 1-5

# create class
class Pet:
    # initialize
    def __init__(self, name, animal_type, age):
        # name, animal_type, and age attributes
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # methods
    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name

    def get_animal_type(self):
        return self.__animal_type

    def set_animal_type(self):
        self.__animal_type

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age
