# Franchesca Marie U. Donadillo
# BSCPE 1-5

import pyfiglet
from termcolor import cprint, colored

# importing class Fan 
from fan_class import Fan

# initialize parameter
fan = Fan(on = False, speed = int(), radius = float(), color = str())

# create object 1
fan_1 = Fan(on = True, speed = 3, radius = 10, color = "yellow")

# create object 2
fan_2 = Fan(on = False, speed = 2, radius = 5, color = "blue")

# Display object 1
title_1 = pyfiglet.figlet_format("FAN #1", font= "lcd")
print("\n" )
cprint(colored(title_1) + "\n--------------------", "red", attrs=["bold"])
print(f"ON: {fan_1._Fan__on}")
print(f"SPEED: {fan_1._Fan__speed} (fast)")
print(f"RADIUS: {fan_1._Fan__radius}")
print(f"COLOR: {fan_1._Fan__color}\n" + "="*40)

# Display object 2
title_2 = pyfiglet.figlet_format("FAN #2", font= "lcd")
print("\n")
cprint(colored(title_2) + "\n--------------------", "cyan", attrs=["bold"])
print(f"ON: {fan_2._Fan__on}")
print(f"SPEED: {fan_2._Fan__speed}")
print(f"RADIUS: {fan_2._Fan__radius}")
print(f"COLOR: {fan_2._Fan__color}\n" + "="*40)
