#You are responsible for writing a program that will convert a given temperature in degrees
#Fahrenheit to degrees Celsius and degrees Kelvin. Your program will round all conversions to a
#precision of four decimal places. Lastly, your program will display the results in a convenient
#table style format.

#Introductory message
print("Welcome to the Temperature Conversion App")

#Asks user for temperature in fahrenheit
f_temp = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

#Converts given temp to celsius and kelvin respectively, rounded to 4 d.p.
f_temp = round(f_temp, 4)
c_temp = round((f_temp - 32) * 5/9, 4)
k_temp = round(c_temp + 273.15, 4)

#Prints out conversion in table format
print(f"\nDegrees Fahrenheit:\t{f_temp}\nDegrees Celsius:\t{c_temp}\nDegrees Kelvin:\t\t{k_temp}")
