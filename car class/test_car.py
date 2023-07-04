# Franchesca Marie U. Donadillo
# BSCPE 1-5

import pyfiglet
from termcolor import cprint, colored

# import Car class from CarClass
from car_class import Car

# initialize parameter
car = Car(year_model = int(), make = str(), speed = 0)

# create car object
car_A = Car(year_model = 2018, make = "Honda", speed = 0)

# call accelarate 5 times and display current speed
title_1 = pyfiglet.figlet_format("ACCELERATE", font="stop")
cprint("\n" +  "="*50 + "\n" + colored(title_1), "red", attrs=["bold"])
counter = 0

while counter < 5:
    car_A.accelerate()
    car_A.get_speed()
    car_A.set_speed()

    counter = counter + 1

# call break method 5 times and display current speed
title_2 = pyfiglet.figlet_format("BREAK", font="stop")
cprint("\n" + "="*50 + "\n" + colored(title_2), "green", attrs = ["bold"])
counter = 5

while counter > 0:
    car_A.break_met()
    car_A.get_speed()
    car_A.set_speed()

    counter = counter - 1

cprint("\n" + colored("="*50), "yellow", attrs=["bold"])