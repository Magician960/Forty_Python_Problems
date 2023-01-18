#You are responsible for writing a program that sorts a list of comma separated numbers as
#either even or odd. Upon sorting the numbers into two groups, your program will then sort each
#group numerically and display the results.

#Welcome message
print("Welcome to the Even Odd Number Sorter App")

#Initialise flag to rerun program
flag = True

while flag:
    #Collect string of numbers
    number_string = input("\nEnter in a string of numbers separated by a comma (,): ")

    #Separate string of numbers
    number_list = number_string.split(",")

    #Convert datatype to int
    number_list = list(map(int, number_list))

    #Initialise even/odd lists
    even_num = []
    odd_num = []

    #Result summary
    print("\n---- Result Summary ----")
    for number in number_list:
        if number % 2 == 0:
            even_num.append(number)
            print(f"\t{number} is even!")
        else:
            odd_num.append(number)
            print(f"\t{number} is odd!")
    
    #Sort lists
    number_list.sort()
    even_num.sort()
    odd_num.sort()

    print(f"\nThe following {len(even_num)} numbers are even:")
    for even_number in even_num:
        print(f"\t{even_number}")

    print(f"\nThe following {len(odd_num)} numbers are odd:")
    for odd_number in odd_num:
        print(f"\t{odd_number}")

    user_input = input("\nWould you like to run this program again (y/n): ").lower()
    if user_input != "y":
        flag = False

#Ending message
print("Thank you for using the program. Goodbye.")