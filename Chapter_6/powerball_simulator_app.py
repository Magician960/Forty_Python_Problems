#You are responsible for writing a program that simulates the Power Ball Lottery. The traditional
#power ball is played by randomly choosing 5 white balls numbered 1 through 69 then randomly
#choosing 1 red ball numbered 1 through 26. The traditional power ball has astronomically low
#odds of winning. Therefore, your program will allow users to adjust the odds by setting how
#many balls the lottery will choose from. Your program will then calculate the odds the user has
#of winning. The user will purchase tickets in a set interval, without purchasing repeated losing
#tickets, until they either win the lottery or choose to give up.

#Import required libraries
import random
from math import comb

#Function to generate powerball numbers
def powerball(num_white_balls, num_red_balls):
    balls_list = []
    white_ball_flag = True
    while white_ball_flag:
        number = random.randint(1, num_white_balls)
        if number not in balls_list:
            balls_list.append(number)
        if len(balls_list) == 5:
            white_ball_flag = False

    balls_list.sort()

    balls_list.append(random.randint(1,num_red_balls))

    return balls_list

#Print introduction
print("--------------------Power-Ball Simulator--------------------")

#Collect lottery simulation parameters
n_white_balls = int(input("\nHow many white-balls to draw from the 5 winning numbers (Normally 69): "))
if n_white_balls < 5:
    n_white_balls = 5
n_red_balls = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))
if n_red_balls < 1:
    n_red_balls = 1

##Calculate probability of winning
#PYTHON 3.8+ ONLY
all_combinations = comb(n_white_balls, 5) * comb(n_red_balls, 1)

#WITHOUT USING LIBRARIES/PYTHON 3.7 AND BELOW
#all_combinations = 1
#for i in range(5):
#    all_combinations *= n_white_balls - i
#all_combinations *= n_red_balls/120

#Print probability
print(f"You have a 1 in {all_combinations} chance of winning the lottery.")

#Collect ticket interval
ticket_interval = int(input("Purchase tickets in what interval: "))
if ticket_interval < 1:
    ticket_interval = 1

print("\n\n---------Welcome to the Power-Ball-----------")
#Generate winning numbers
winning_balls_list = powerball(n_white_balls, n_red_balls)

print("\nTonight's winning numbers are: ", end="")
for winning_ball in winning_balls_list:
    print(winning_ball, end=" ")

input("\nPress 'Enter' to begin purchasing tickets!!!")

#Randomly generate user tickets
round_flag = True
tickets_generated = 0
all_tickets_generated = []
#While loop to generate tickets for each batch
while round_flag:
    ticket_flag = True
    while ticket_flag:
        user_ticket = powerball(n_white_balls, n_red_balls)
        #Disregard ticket if already generated previously
        if user_ticket not in all_tickets_generated:
            all_tickets_generated.append(user_ticket)
        else:
            print("Losing ticket generated, disregard...")
            ticket_flag = False
            break
        tickets_generated += 1
        print(user_ticket)
        #End loop if user wins
        if user_ticket == winning_balls_list:
            lost_powerball = False
            print("Winning ticket numbers: ", end="")
            for winning_ball in winning_balls_list:
                print(winning_ball, end=" ")
            print(f"\nPurchased a total of {tickets_generated} tickets.")
            ticket_flag = False
            round_flag = False
            break
        #Ask user for repeat if lost, else quit program
        if tickets_generated % ticket_interval == 0:
            print(f"{tickets_generated} tickets purchased so far with no winners...")
            response = input("\nKeep purchasing tickets (y/n): ").lower().strip()
            if response != "y":
                print(f"\nYou bought {tickets_generated} tickets and still lost!\nBetter luck next time!")
                ticket_flag = False
                round_flag = False
