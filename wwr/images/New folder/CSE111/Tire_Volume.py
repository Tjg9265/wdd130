from datetime import datetime
import math
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
print(f"The approximate volume is {volume:.2f} liters")
current_date = datetime.now().date()
with open("volumes.txt", "at") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}")
    buy_tires = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()
    if buy_tires == "yes":
        phone = input("Please enter your phone number: ")
        file.write(f", {phone}")
    file.write("\n")