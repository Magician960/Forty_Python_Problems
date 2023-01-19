#You are responsible for writing a program that generates all factors of a given number. Your
#program will display the factors individually and give a mathematical summary of how different
#pairs of factors can be multiplied together to get the given number.

#Welcome message
print("Welcome to the Factor Generator App")

#Initialise Boolean for stopping program
flag = True

while flag:
    #Ask for number
    num = int(input("\nEnter a number to determine all factors of that number: "))

    #Initialise list to hold factors
    factors = []

    #Print all factors
    print(f"\nFactors of {num} are:")

    counter = 1
    while counter <= num:
        if num % counter == 0:
            print(counter)
            factors.append(counter)
        counter += 1

    #Print mathematical summary
    print("\nIn summary:")
    while factors:
        print(f"{factors[0]} * {factors[-1]} = {num}")
        factors.pop(0)
        if factors:
            factors.pop(-1)
    
    #Ask user to end program
    answer = input("\nRun again (y/n): ").lower()
    if answer != "y":
        flag = False

#Ending statement
print("Thank you for using the program. Have a great day.")