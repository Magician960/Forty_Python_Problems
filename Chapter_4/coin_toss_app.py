#You are responsible for writing a program that will simulate flipping a coin n number of times.
#Your program will present the user an option to see the result of each individual flip. Your
#program will also inform the user any time the number of heads flipped is equal to the number of
#tails flipped. Upon completion of all flips, your program will provide a summary table that shows
#the number and percentage of each flip.

import random

#Welcome message
print("Welcome to the Coin Toss App")

#Count variables
heads = 0
tails = 0
total_flips = 0

#Set user's paramters for program
print("\nI will flip a coin a set number of times")
no_of_flips = int(input("How many times would you like me to flip the coin: "))
all_results = input("Would you like to see the result of each flip (y/n): ").lower()

#Coin flip functions

print("\nFlipping!!!\n")

if all_results.startswith("n"):
    for n in range(1, no_of_flips + 1):
        if random.randint(0,1) == 0:
            tails += 1
            total_flips += 1
        else:
            heads += 1
            total_flips += 1
        if heads == tails:
            print(f"At {n} flips, the number of heads and tails were equal at {tails} each.")

elif all_results.startswith("y"):
    for n in range(1, no_of_flips + 1):
        if random.randint(0,1) == 0:
            print("TAILS")
            tails += 1
            total_flips += 1
        else:
            print("HEADS")
            heads += 1
            total_flips += 1
        if heads == tails:
            print(f"At {n} flips, the number of heads and tails were equal at {tails} each.")


#Display summary table
print(f"Results Of Flipping A Coin {no_of_flips} Times")
print("\nSide\tCount\tPercentage")
print(f"Heads\t{heads}/{total_flips}\t{round((heads/total_flips*100), 2)}%")
print(f"Tails\t{tails}/{total_flips}\t{round((tails/total_flips*100), 2)}%")