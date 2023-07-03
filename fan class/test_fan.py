# Franchesca Marie U. Donadillo
# BSCPE 1-5

# importing class Fan 
from fan_class import Fan

# initialize parameter
fan = Fan(on = False, speed = int(), radius = float(), color = str())

# create object 1
fan_1 = Fan(on = True, speed = 3, radius = 10, color = "yellow")

# create object 2
fan_2 = Fan(on = False, speed = 2, radius = 5, color = "blue")

# Display object 1
print("\nFAN #1\n--------------------")
print(f"ON: {fan_1._Fan__on}")
print(f"SPEED: {fan_1._Fan__speed} (fast)")
print(f"RADIUS: {fan_1._Fan__radius}")
print(f"COLOR: {fan_1._Fan__color}\n=====================")

# Display object 2
print("\nFAN #2\n--------------------")
print(f"ON: {fan_2._Fan__on}")
print(f"SPEED: {fan_2._Fan__speed}")
print(f"RADIUS: {fan_2._Fan__radius}")
print(f"COLOR: {fan_2._Fan__color}\n=====================")
