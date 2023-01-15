#You are responsible for writing a program that will simulate registering to vote. If a user is 18 or
#older, your program will present them with a list of potential political parties to register for. Upon
#choosing a party, your program will confirm that the user has registered and print a specific
#message depending on the party joined.

#Initialise political party list
party_list = ["Labor", "Liberal", "Greens", "National", "Independent"]

#Welcome message
print("Welcome to the Voter Registration App")

#Ask user's name and age
name = input("\nPlease enter your name: ").title().strip()

if int(input("Please enter your age: ")) < 18:
    print("\nYou are not old enough to vote.")
    quit()

print(f"\nCongratulations {name}! You are old enough to register to vote.")

#Print party list
print("\nHere is a list of political parties to join")

for party in party_list:
    print(f"\t- {party}")

#Ask user for party affiliation
user_party = input("What party would you like to join: ").title().strip()

#Comment on user's choice
if user_party in party_list:
    print(f"\nCongratulations {name}! You have joined the {user_party} party!")
    if user_party.startswith("L"):
        print("That is a major party!")
    elif user_party == "Independent":
        print("You are an independent person!")
    else:
        print("That is not a major party!")
else:
    print("That party doesn't exist")