#You are responsible for writing a program that will conduct a poll on a yes or no issue. Upon
#starting the program a user will be prompted for an issue to vote on, the number of voters, and a
#password to view the poll results. Your program will then conduct the poll. Each time a user
#votes, your program will ask for the voters full name to verify that they have not yet voted. If the
#voter has not yet voted, they will be presented with the issue and can vote yes or no. The vote
#will be recorded. Once the number of voters specified by the user has been reached, the poll
#will close and a summary will be displayed. If the user enters the correct password a result of
#each voters name and how they voted will be displayed.

#Initialise required libraries
from operator import countOf

#Welcome message
print("Welcome to the Yes or No Issue Polling App")

#Voting function
def vote():
    full_name = input("\nEnter your full name: ").title().strip()
    if full_name in voters.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print(f"Here is our issue: {issue}")
        answer = input("What do you think...yes or no: ").lower().strip()
        if answer == "y":
            answer = "yes"
        elif answer == "n":
            answer = "no"
        voters[full_name] = answer
        if answer != "yes" and answer != "no":
            print("That is not a yes or no answer, but okay...")
        print(f"Thank you {full_name}! Your vote of {answer} has been recorded.")
        

#Initialise dictionary
voters = {}

#Ask for an issue
issue = input("\nWhat is the yes or no issue you will be voting on today: ").strip()

#Ask for number of voters
voter_number = int(input("What is the number of votes you will allow on the issue: "))
if voter_number < 1:
    print("Please enter a valid number")
    quit()

#Create user password
password = input("Enter a password for polling results: ").strip()

#Loop vote function for all voters
for i in range(0, voter_number):
    vote()

#Print all voter names
print(f"\nThe following {len(voters)} people voted:")
for voter in voters.keys():
    print(voter)

#Calculate vote result
print(f"\nOn the following issue: {issue}")
total_yes = countOf(voters.values(), "yes")
total_no = countOf(voters.values(), "no")
if total_yes > total_no:
    print(f"Yes wins! {total_yes} votes to {total_no}")
elif total_no > total_yes:
    print(f"No wins! {total_no} votes to {total_yes}")
else:
    print(f"It was a tie! {total_yes} votes to {total_no}")

#Check user password to display dictionary
if input("\nTo see the voting results enter the admin password: ") == password:
    for voter, response in voters.items():
        print(f"Voter: {voter}\t\tVote: {response}")
else:
    print("Sorry, that is not the correct password. Goodbye...")

#Farewall message
print("\nThank you for using the Yes or No Issue Polling App.")