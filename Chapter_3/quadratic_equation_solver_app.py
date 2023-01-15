#You are responsible for writing a program that will display the solutions to any number of
#quadratic equations. Your program will ask the user how many quadratic equations they would
#like to solve, ask for the coefficients of the equation in the standard form of ax2 + bx + c = 0 ,
#solve for x, and then display the solutions. Your program will allow for both real and complex
#solutions.

import cmath

#Quadratic equation solver function
def quadratic_solver():
    print(f"\nSolving equation #{i}\n---------------------------------------------------------------\n")
    a = float(input("Please enter your value of a(coefficient of x^2): "))
    b = float(input("Please enter your value of b(coefficient of x): "))
    c = float(input("Please enter your value of c(coefficient): "))

    print(f"\nThe solutions to {a}x^2 + {b}x + {c} = 0 are:")

    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/ 2*a
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/ 2*a
    print(f"\n\tx1 = {x1}\n\tx2 = {x2}")

#Introductory message
print("Welcome to the Quadratic Equation Solver App.")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0\nYour solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj\nWhere a is the real portion and bj is the imaginary portion.")

#Ask user for no. of equations
no_of_equations = int(input("\nHow many equations would you like to solve today: "))

#Call quadratic solver function according to number of times user asked

for i in range(1, no_of_equations + 1):
    quadratic_solver()

#Ending message
print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")

