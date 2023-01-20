#You are responsible for writing a program that simulates a calculator application that will take in
#any two numbers, and a basic mathematical operation (addition, subtraction, multiplication,
#division, or exponentiation), perform that operation, print a lexical statement of the operation,
#and return a mathematical statement that describes the mathematical results. Upon completion,
#your program will print out a history of all calculations performed including any error messages
#that may have occurred such as division by zero.

#Welcome message
print("Welcome to the Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed")

#Addition function
def add(first_num, second_num):
    result = first_num + second_num
    print(f"The sum of {first_num} and {second_num} is {result:,}")
    calc_history.append(f"{first_num} + {second_num} = {result:,}")

#Subtraction function
def subtract(first_num, second_num):
    result = first_num - second_num
    print(f"The difference of {first_num} and {second_num} is {result:,}")
    calc_history.append(f"{first_num} - {second_num} = {result:,}")

#Multiplication function
def multiply(first_num, second_num):
    result = first_num * second_num
    print(f"The product of {first_num} and {second_num} is {result:,}")
    calc_history.append(f"{first_num} * {second_num} = {result:,}")

#Division function
def divide(first_num, second_num):
    if second_num == 0:
        print("You cannot divide by zero.")
        calc_history.append("DIV ERROR")
    else:
        result = first_num / second_num
        print(f"The quotient of {first_num} and {second_num} is {result:,}")
        calc_history.append(f"{first_num} / {second_num} = {result:,}")

#Exponent function
def power(first_num, second_num):
    result = first_num ** second_num
    print(f"The result of {first_num} raised to the {second_num} power is {result:,}")
    calc_history.append(f"{first_num} ** {second_num} = {result:,}")

#Operations error
def opp_error():
    print("That is not a valid operation. Try again.")
    calc_history.append("OPP ERROR")

#Initialise program loop
app_loop = True

#Initialise calculation summary
calc_history = []

#Main program loop
while app_loop:
    #Ask for user parameters
    num_1 = float(input("\nEnter a number: "))
    num_2 = float(input("Enter a number: "))
    
    #Ask for operation
    operation = input("Enter an operation (addition,subtraction,multiplication,division,exponentiation):\n").lower().strip()
    if operation.startswith("a"):
        add(num_1, num_2)
    elif operation.startswith("sub"):
        subtract(num_1, num_2)
    elif operation.startswith("m"):
        multiply(num_1, num_2)
    elif operation.startswith("d"):
        divide(num_1, num_2)
    elif operation.startswith("e"):
        power(num_1, num_2)
    else:
        opp_error()

    #Ask user to end program
    response = input("Would you like to run the program again (y/n): ").lower().strip()
    if response != "y":
        app_loop = False

#Print calculation summary
print("\nCalculation Summary:")
for calc in calc_history:
    print(calc)

#Ending message
print("\nThank you for using the Python Calculator App. Goodbye.")