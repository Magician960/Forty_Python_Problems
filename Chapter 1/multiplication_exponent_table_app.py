#You are responsible for writing a program that displays a multiplication table and exponentiation
#table for any given number. Each table should show mathematical results for operations
#performed with the given number and integers from 1 to 9. The program will then print a series
#of messages to the user describing how cool mathematics truly is.

#Introductory message
print("Welcome to the Multiplication/Exponent Table App")

#Ask for user's name
name = input("\nWhat is your name: ").title().strip()

#Ask for number
num = float(input("What number would you like to work with: "))


#Print multiplication table with number from 1 to 9
print(f"\nMultiplication Table for {num}\n")

for i in range(1,10):
    print(f"\t{i} * {num} = {round(i * num, 4)}")

#Print exponent table with number from 1 to 9
print(f"\nExponent Table for {num}\n")

for i in range(1,10):
    print(f"\t{num} ** {i} = {round(num ** i, 4)}")

#Print various messages
msg = f"{name} Math is cool!"

print(f"\n{msg}")
print(f"\t{msg.lower()}")
print(f"\t\t{msg.title()}")
print(f"\t\t\t{msg.upper()}")