#You are responsible for writing a program that will simulate an online banking application. A
#user will create an account with your fictitious bank. The account will include a savings account
#and a checking account. Users will then be able to make deposits or withdrawals from either
#account as long as the remaining balance is non negative.

#Function to get user info
def collect_info():
    #Initial set-up
    full_name = input("Hello, what is your name: ").title().strip()
    savings = round(float(input("How much money would you like to set up your savings account with: ")), 2)
    checking = round(float(input("How much money would you like to set up your checking account with: ")), 2)

    #Initialise account dictionary
    account = {full_name:  {"savings_acct": savings,
                            "checking_acct": checking},
                }
    return account

#Function to print account details
def acct_summary(acct):
    print("\nCurrent Account Information:")
    for name, details in acct.items():
        print(f"Name: {name}")
        print(f"Savings: ${details['savings_acct']}")
        print(f"Checking: ${details['checking_acct']}")

#Function to perform a deposit
def deposit(acct_dict, acct, money_amount):
    for name, accounts in acct_dict.items():
        #Determine which account to deposit into
        if acct == "savings":
            acct_dict[name]["savings_acct"] += money_amount
        else:
            acct_dict[name]["checking_acct"] += money_amount
        
        print(f"\nDeposited ${money_amount} into {name}'s {acct} account.")
        
    

#Function to perform a withdrawal
def withdrawal(acct_dict, acct, money_amount):
    for name, accounts in acct_dict.items():
        #Determine which account to withdraw from
        if acct == "savings":
            #Check that withdrawal won't leave user with a negative balance
            if acct_dict[name]["savings_acct"] - money_amount > 0:
                acct_dict[name]["savings_acct"] -= money_amount
                print(f"\nWithdrew ${money_amount} from {name}'s {acct} account.")
            else:
                print(f"\nSorry, by withdrawing ${money_amount} you will have a negative balance")
        else:
            if acct_dict[name]["checking_acct"] - money_amount > 0:
                acct_dict[name]["checking_acct"] -= money_amount
                print(f"\nWithdrew ${money_amount} from {name}'s {acct} account.")
            else:
                print(f"\nSorry, by withdrawing ${money_amount} you will have a negative balance")

#Welcome message
print("Welcome to the Python First National Bank.")

#Collect user info
user_info = collect_info()

#Initialise program loop
program_loop = True

#Main program
while program_loop:
    #Print account details
    acct_summary(user_info)

    #Collect user parameters
    acct_name = input("\nWhat account would you like to access (Savings or Checking): ").lower().strip()
    transaction_type = input("What type of transaction would you like to make (Deposit or Withdrawal): ").lower().strip()
    amount = float(input("How much money: $"))
    if acct_name == "savings" or acct_name == "checking":
        if transaction_type == "deposit":
            deposit(user_info, acct_name, amount)
        elif transaction_type == "withdrawal":
            withdrawal(user_info, acct_name, amount)
        else:
            print("\nI'm sorry, we cannot do that for you today.")
    else:
        print("\nI'm sorry, we cannot do that for you today.")
    #Ask user to end program
    response = input("Would you like to make another transaction (y/n): ").lower().strip()
    if response != "y":
        program_loop = False

#Ending message
print("\nThank you. Have a great day!")