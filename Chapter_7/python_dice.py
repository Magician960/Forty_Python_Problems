#You are responsible for writing a program that will roll a given number of dice of any number of
#sides and sum the total. Your program will continue to run until the user desires to quit.

#Import required libraries
import random

#Print welcome message
print("Welcome to the Python Dice App")

#Function to roll dice
def roll_dice(n_sides, n_dice):
    #Initialise empty list to hold dice rolled
    rolled_dice = []

    print(f"\nYou rolled {n_dice} {n_sides} sided dice.")
    print("\n-----Results are as followed-----")

    #Roll dice and store result
    for i in range(0,n_dice):
        result = random.randint(1,n_sides)
        print(f"\t{result}")
        rolled_dice.append(result)
    return rolled_dice

#Function to sum dice result total
def sum_dice(dice_list):
    print(f"The total value of your roll is {sum(dice_list)}")

#Function to end program
def end_program():
    response = input("\nWould you like to roll again (y/n): ").lower().strip()
    if response != "y":
        print("\nThank you for using the Python Dice App.")
        return False
    else:
        return True

#Initialise flag variable for program looping
game_loop = True

while game_loop:
    #Collect user parameters
    num_sides = int(input("\nHow many sides would you like on your dice: "))
    num_dice = int(input("How many dice would you like to roll: "))

    #Roll dice
    dice_results = roll_dice(num_sides, num_dice)

    #Calculate dice total
    sum_dice(dice_results)

    #Ask user to repeat program
    game_loop = end_program()