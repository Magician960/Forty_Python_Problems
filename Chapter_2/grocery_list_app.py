#You are responsible for writing a program that will simulate a grocery shopping list. Your
#program will start with two items on the shopping list, meat and cheese, and then allow a user to
#dd three new items to the list. To simulate shopping, your program will ask the user what item
#they just purchased and then remove the item from the shopping list. Upon having only two
#items in the shopping list, your program will inform the user that the store is out of a particular
#item and prompt the user to replace the item with a new item. You will use the datetime library
#to display the current date and time the shopping is taking place in mm/dd hh:mm format.

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%m/%d %H:%M")

#Function to simulate shopping and ticking off list items
def shopping(list):
    print(f"\nCurrent grocery list: {len(list)} items\n{list}")
    removed_food = input("What food did you just buy: ").title()
    list.remove(removed_food)
    print(f"Removing {removed_food} from list...")

#Initialise list
grocery = ["Meat", "Cheese"]

#Welcome message
print(f"Welcome to the Grocery List App.\nCurrent Date and Time: {dt_string}")
print(f"You currently have {grocery[0]} and {grocery[1]} in your list.\n")

#Add items to shopping list
while len(grocery) != 5:
    grocery.append(input("Type of food to add to the grocery list: ").title())

#Display and sort completed list
print(f"\nHere is your grocery list:\n{grocery}")
grocery.sort()
print(f"Here is your grocery list sorted:\n{grocery}")

print("\nSimulating grocery shopping...")

#Removing items from shopping list one-by-one
while len(grocery) != 2:
    shopping(grocery)

#Replace item on shopping list with user input
print(f"\nCurrent grocery list: {len(grocery)} items\n{grocery}\n\nSorry, the store is out of {grocery[-1]}")
grocery.pop()
grocery.insert(0, input("What food would you like instead: ").title())

print(f"\nHere is what remains on your grocery list:\n{grocery}")

