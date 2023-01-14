#You are responsible for writing a program that will convert any given speed in miles per hour to
#a more metric friendly unit of meters per second. All calculations should be rounded to a set
#decimal precision of 2 decimal places.

#Introductory message
print("Welcome to the Miles Per Hour Conversion App")

#Asks user to speed and convert str into float
mph_speed = float(input("\nWhat is your speed in miles per hour:"))

#Calculate metres per second
converted_speed = round(mph_speed / 2.2369362912, 2)

#Prints out conversion
print(f"Your speed in meters per second is {converted_speed}")