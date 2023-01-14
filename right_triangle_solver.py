#You are responsible for writing a program that will calculate the hypotenuse and area of a right
#triangle given its two bases. Your program will round all calculations to a precision of three
#decimal places and provide a summary of the mathematical results.

# Import math Library
import math

#Introductory message
print("Welcome to the Right Triangle Solver App")

#Ask user for 2 sides of a right-angled triangle
leg1 = float(input("\nWhat is the first leg of the triangle: "))
leg2 = float(input("What is the second leg of the triangle: "))

#Calculate the hypotenuse and area based off user's input
hypotenuse = round(math.sqrt(leg1 ** 2 + leg2 ** 2), 3)
area = round(1/2 * leg1 * leg2, 3)

#Print out calculations
print(f"\nFor a triangle with legs of {leg1} and {leg2} the hypotenuse is {hypotenuse}.")
print(f"For a triangle with legs of {leg1} and {leg2} the area is {area}.")
