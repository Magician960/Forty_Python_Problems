#You are responsible for writing a program that will either determine if a given number is prime or
#display all prime numbers within a given range of values. When determining all prime numbers
#within a given range, your program will time the process and report how long the calculations
#took to the user. It is important to time certain processes within our programs so we can so how
#efficient our code is.

#importing the module
import time

#check prime function
def check_prime(number):

    #Initialise boolean to hold factors
    factors = False

    #Loop through range to collect factors
    for counter in range(2,number):
        if number % counter == 0:
            factors = True
            break

    #Write result statement
    if factors:
        print(f"{number} is not prime!")
    else:
        print(f"{number} is prime!")

#list all primes function:
def list_primes(lower,upper):

    #Initialise list to hold prime numbers
    prime_numbers = []

    # records start time
    start = time.perf_counter()

    #Loop through range to collect prime_factors
    for potential_prime in range(lower, upper + 1):
        #Initialise boolean to hold factors
        factors = False
        for counter in range(2,potential_prime):
            if potential_prime % counter == 0:
                factors = True
                break
        if factors == False:
            prime_numbers.append(potential_prime)
    
    #Remove 1 from prime_numbers if present
    if 1 in prime_numbers:
        prime_numbers.remove(1)
    # record end time
    end = time.perf_counter()

    #print elapsed time
    print(f"\nCalculations took a total of {end - start} seconds.")
    print(f"The following numbers between {lower} and {upper} are prime.")
    placeholder = input("Press enter to continue.")
    for prime_number in prime_numbers:
        print(prime_number)

#Welcome message
print("Welcome to the Prime Number App")

#Initialise flag to determine end of program
flag = True

while flag:
    #User options
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range")

    #User choice
    choice = int(input("Enter your choice 1 or 2: "))

    #Determine whether specific number is prime:
    if choice == 1:
        #User number
        user_number = int(input("Enter a number to determine if it is prime or not: "))

        check_prime(user_number)

    #Print all prime numbers in a given range
    elif choice == 2:
        lower_bound = int(input("\nEnter the lower bound of your range: "))
        upper_bound = int(input("Enter the upper bound of your range: "))

        list_primes(lower_bound, upper_bound)

    #Exception handling
    else:
        print("\nThat is not a valid option")

    #Ask user to end program
    answer = input("Would you like to run the program again (y/n): ")
    if answer != "y":
        flag = False

#Ending message
print("\nThank you for using the program. Have a nice day.")
