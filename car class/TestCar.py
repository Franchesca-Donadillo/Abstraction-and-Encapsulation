# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import Car class from CarClass
from CarClass import Car

# initialize parameter
car = Car(year_model = int(), make = str(), speed = 0)

# create car object
car_A = Car(year_model = 2018, make = "Honda", speed = 0)

# call accelarate 5 times and display current speed
counter = 0

while counter < 5:
    car_A.accelerate()
    car_A.get_speed()
    car_A.set_speed()

    counter = counter + 1

# call break method 5 times and display current speed
