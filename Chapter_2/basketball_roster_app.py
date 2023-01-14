#You are responsible for writing a program that will build and display a basketball roster based off
#user input. Your program will then simulate an injury to a specific player in the roster and
#prompt the user to update the roster. Upon updating the roster, your program will display the
#final roster and wish the newly add player good luck.

#Initialise roster dictionary
roster = dict.fromkeys(["Point Guard","Shooting Guard","Small Forward","Power Forward","Center"])

#Print roster function
def print_roster(dict):
    print("\n\tYour starting 5 for the upcoming basketball season")
    for role, player in roster.items():
        if role == "Center":
            print(f"\t\t{role}:\t\t\t\t{player}")
        else:
            print(f"\t\t{role}:\t\t\t{player}")


#Print welcome message
print("Welcome to the Basketball Roster Program\n")

#Fill dictionary with players via user input
for role, player in roster.items():
    roster.update({role: input(f"Who is your {role.lower()}: ").title().strip()})

print_roster(roster)

#Asks user to replace small forward
injured_player = roster.get("Small Forward")
print(f"\nOh no, {injured_player} is injured.\nYour roster only has {len(roster) - 1} players.")
roster.update({"Small Forward": input(f"Who will take {injured_player}'s spot: ").title().strip()})

#Introducing new player
print_roster(roster)
new_player = roster.get("Small Forward")
print(f"\nGood luck {new_player} you will do great!\nYour roster now has {len(roster)} players.")