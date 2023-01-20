#You are responsible for writing a program that gathers information about a loan such as starting
#principal, interest rate, and desired monthly payment. From this information, your program will
#first determine if it is possible to pay off the loan based on the desired monthly payment. If it is
#possible, your program will simulate making monthly payments until the loan is completely paid
#off. Your program will then display statistics such as how long it took to pay the loan off, the
#total amount spent on the loan, and the amount spent on interest. For simplicity, we will
#assume that the loan compounds once a month, or twelve times in a year. Upon completion of
#paying off the Loan, your program will make a graph showing the rate of change of the principal
#to time using the matplotlib library.

#Import required libraries
import matplotlib.pyplot as plt

#Initialise dictionary for user
user_loan = {}

#Function to collect user loan info
def get_loan_info(dict):
    dict["Principal"] = float(input("\nEnter the loan amount: "))
    dict["Rate"] = float(input("Enter the interest rate: ")) / 100
    dict["Monthly Payment"] = float(input("Enter the desired monthly payment amount: "))
    dict["Money Paid"] = 0

#Function to print user loan info
def print_loan_info(dict, counter):
    print(f"\n----Loan information after {counter} months----")
    for key, value in dict.items():
        print(f"{key}: {value:,}")

#Function to add interest to loan
def add_interest(dict):
    dict["Principal"] += dict["Principal"] * dict["Rate"]/12

#Function to make a payment
def make_payment(dict):
    dict["Principal"] -= dict["Monthly Payment"]
    dict["Money Paid"] += dict["Monthly Payment"]

#Function to print end-of-loan summary statistics
def loan_summary(dict, counter, history):
    print(f"\nCongratulations! You paid off your loan in {counter} months!")
    print(f"Your initial loan was ${history[0][1]:,} at a rate of {dict['Rate'] * 100}%.")
    print(f"Your monthly payment was ${dict['Monthly Payment']:,}")
    print(f"You spent ${round(dict['Money Paid'], 2):,} total.")
    print(f"You spent ${round(dict['Money Paid'] - history[0][1], 2):,} on interest!")

#Function to record payment
def record_payment(dict, counter, history):
    history.append((counter,dict["Principal"]))

#Function to plot loan history
def plot_loan(dict, history):
    zip(*history)
    plt.plot(*zip(*history))
    plt.title(f"{dict['Rate']*100}% Interest With ${dict['Monthly Payment']:,} Monthly Payment", fontsize=14)
    plt.xlabel("Month Number", fontsize=14)
    plt.ylabel("Principal of Loan", fontsize=14)
    plt.show()

#Welcome message
print("Welcome to the Loan Calculator App")

#Collect loan parameters
get_loan_info(user_loan)

#Initialise list for loan history
loan_history = []

#Print initial loan info
month = 0
print_loan_info(user_loan, month)
record_payment(user_loan, month, loan_history)
input("Press 'enter' to begin paying off your loan.")

#Program loop
while True:
    #Check if loan is payable given parameters
    if user_loan["Principal"] * user_loan["Rate"]/12 > user_loan["Monthly Payment"]:
        add_interest(user_loan)
        print_loan_info(user_loan, month)
        print("\nYou will never pay off your loan!!!")
        print("You cannot get ahead of the interest!! :-(")
        break

    #Check if this is their final payment
    if user_loan["Principal"] <= user_loan["Monthly Payment"]:
        user_loan["Money Paid"] += user_loan["Principal"]
        user_loan["Principal"] = 0
        month += 1
        record_payment(user_loan, month, loan_history)
        print_loan_info(user_loan, month)
        loan_summary(user_loan, month, loan_history)
        plot_loan(user_loan, loan_history)
        break

    #Make a loan payment
    add_interest(user_loan)
    make_payment(user_loan)

    #Increment month counter
    month += 1

    #Record payment
    record_payment(user_loan, month, loan_history)

    #Print updated loan info
    print_loan_info(user_loan, month)