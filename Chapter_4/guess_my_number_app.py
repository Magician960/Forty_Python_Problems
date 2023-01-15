#You are responsible for writing a program that will play the classic “Hi Low” game. Your
#program will randomly pick a number between 1 and 20. Users will then guess the number.
#With each guess, your program will respond that the user’s guess is either too high or too low.
#When the user guesses correct, or after 5 guesses, your program will end the game and
#summarize the results.

import random

random_number = random.randint(1, 20)
guess_count = 0
player_guess = 0

#Welcome message
print("Welcome to the Guess My Number App")

#Ask user's name
name = input("\nHello! What is your name: ").title().strip()

#Introduce game
print(f"Well {name}, I am thinking of a number between 1 and 20")

#TESTING ONLY, REMOVE IN FINAL VERSIOn
print(random_number)

#Number guessing function
while player_guess != random_number and guess_count != 5:
    player_guess = int(input("\nTake a guess: "))
    if player_guess < random_number:
        print("Your guess it too low")
    else:
        print("Your guess is too high")
    guess_count += 1

#Ending comment
if player_guess == random_number:
    print(f"\nGood job {name}! You guessed my number in {guess_count} guesses!")
else:
    print(f"\nGame Over. The number I was thinking of was {random_number}.")
