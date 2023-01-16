#You are responsible for writing a program that will simulate playing the classic game Rock,
#Paper, Scissors against computer AI. Your program will ask the user how many rounds of the
#game they would like to play, simulate each round, keep score, and determine an overall
#winner. Your program will also print the classic phrases such as “Paper covers rock” or
#“Scissors cut paper”.

import random


#Initialise variables
player_score = 0
computer_score = 0

#Round win function
def player_win():
    print(f"\tYou win round {round}")
    global player_score
    player_score += 1
def computer_win():
    print(f"\tComputer wins round {round}")
    global computer_score
    computer_score += 1

#Game Function
def game():
    #Print current round
    print(f"\nRound {round}")

    #Display current score
    global player_score
    global computer_score
    print(f"Player: {player_score}\tComputer: {computer_score}")

    #Ask for user action
    player = input("Time to pick...rock, paper, scissors: ").lower()

    #Calculate computer action
    computer = ""
    computer_number = random.randint(1,3)
    if computer_number == 1:
        computer = "rock"
    elif computer_number == 2:
        computer = "paper"
    else:
        computer = "scissors"
    
    #Print round results
    print(f"\tComputer: {computer}")
    print(f"\tPlayer: {player}")
    if player == computer:
        print("\tIt is a tie, how boring!\n\tThis round was a tie")
    elif player == "rock" and computer == "scissors":
        print("\tRock breaks scissors!")
        player_win()
    elif player == "rock" and computer == "paper":
        print("\tPaper covers rock!")
        computer_win()
    elif player == "scissors" and computer == "rock":
        print("\tRock breaks scissors!")
        computer_win()
    elif player == "scissors" and computer == "paper":
        print("\tScissors cut paper!")
        player_win()
    elif player == "paper" and computer == "scissors":
        print("\tScissors cut paper!")
        computer_win()
    elif player == "paper" and computer == "rock":
        print("\tPaper covers rock!")
        player_win()
    else:
        print("\tThat is not a valid game option!")
        print("\tComputer gets the point!")
        computer_score += 1

#Welcome message
print("Welcome to a game of Rock, Paper, Scissors")

#Ask for no. of rounds to play
no_of_rounds = int(input("How many rounds would you like to play: "))

#Game function
for round in range(1,no_of_rounds+1):
    game()

#End-of-game Summary
print("\nFinal Game Results")
print(f"\tRounds Played: {no_of_rounds}")
print(f"\tPlayer Score: {player_score}")
print(f"\tComputer Score: {computer_score}")

if player_score > computer_score:
    print("\tWinner: PLAYER!!!")
elif player_score < computer_score:
    print("\tWinner: Computer :-(")
else:
    print("\tWinner: Tie")