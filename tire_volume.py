import math
from datetime import datetime

#Dictionary to store tires sizes and prices
tire_prices = {
    (205, 60, 16): 70,
    (205, 55, 16): 80,
    (195, 65, 15): 73,
    (235, 60, 16): 104,
    (215, 60, 16): 85,
    (225, 65, 17): 84
}
# This program reads from the keyboard the three numbers for a tire
# and computes and outputs the volume of space inside that tire.
# Get the user to insert the width, ratio, and diameter of the tire.

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
#formula to calculate the tire volume
volume = math.pi*width**2*aspect_ratio*(width*aspect_ratio+2540*diameter)/10000000000
#round to 2 decimal digits
volume = round(volume, 2)
print(f"The approximate volume is {volume} liters.")

price = None

if (width, aspect_ratio, diameter) == (205, 60, 16):
    price = 70.00
elif (width, aspect_ratio, diameter) == (205, 55, 16):
    price = 80.00
elif (width, aspect_ratio, diameter) == (195, 65, 15):
    price = 73.00   
elif (width, aspect_ratio, diameter) == (235, 60, 16):
    price = 104.00
elif (width, aspect_ratio, diameter) == (215, 60, 16):
    price = 85.00
elif (width, aspect_ratio, diameter) == (225, 65, 17):
    price = 84.00        
else:
    print("Price not available")

price = tire_prices.get((width, aspect_ratio, diameter), "Price not available")

if isinstance(price, (int, float)):
    print(f"Price ${price:.2f}")
else:
    print(f"Price: {price}")    

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    print(f'{current_date_and_time: %Y-%m-%d}', file=volumes_file, end=", ", flush=False, sep=" ")
    print(width, file=volumes_file, end=", ", flush=False, sep=" ",)
    print(aspect_ratio, file=volumes_file, end=", ", flush=False, sep=" ")
    print(diameter, file=volumes_file, end=", ", flush=False, sep=" ")
    print(volume, file=volumes_file)

