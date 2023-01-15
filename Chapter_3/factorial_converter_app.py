#You are responsible for writing a program that will calculate the factorial of any given number.
#Your program will display the mathematical relationship of the factorial. It will then use the math
#library to compute the value of the given factorial. Lastly, your program will use its own
#algorithm to compute the value of the given factorial and compare the results.

import math

#Welcome message
print("Welcome to the Factorial Calculator App")

#Ask user for factorial number
num = int(input("\nWhat number would you like to compute the factorial of? "))

#Display factorial equation
factorial_list = list(range(1, num+1))
factorial_list_string = [str(x) for x in factorial_list]
factorial_equation = "*".join(factorial_list_string)
print(f"{num}! = {factorial_equation}")

#Calculate factorial using math library
print(f"Here is the result from the math library:\nThe factorial of {num} is {math.factorial(num)}!")

#Calculate factorial independently
x = 1
for number in factorial_list:
    x *= number
print(f"\nHere is the result from my own algorithm:\nThe factorial of {num} is {x}!")

#Compare both calculations
if math.factorial(num) == x:
    print(f"\nIt is shown twice that {num}! = {x} (with excitement)")