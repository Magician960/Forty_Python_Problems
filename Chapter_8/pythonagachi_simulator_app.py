#You will be responsible for writing a program that simulates the behavior of a retro 90’s
#Tamagachi toy. You program will allow a user to create their own creature, give it a name, and
#care for it until it unfortunately parishes. Users will monitor the creatures hunger, boredom,
#tiredness, and dirtiness and take actions to prevent any of the categories from getting to high. If
#the categories get too high there will be unfortunate consequences.

#Import required libraries
import random

#Define pet class
class Pet():
    #Initialise pet stats
    def __init__(self, level, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food_inventory = 6 - level
        self.current_status = "Awake"
    #Method to update pet stats
    def update_stats(self, level):
        self.current_status = "Awake"
        self.boredom += random.randint(1,level)
        if self.boredom > 10:
            print(f"{self.name} is so bored he is ignoring your instructions")
            self.current_status = "Bored"
            self.boredom = 10
        self.tiredness += random.randint(1,level)
        if self.tiredness > 10:
            print(f"{self.name} has fallen asleep!")
            self.current_status = "Asleep"
            self.tiredness = 10
        self.dirtiness += random.randint(1,level)
        if self.dirtiness >10:
            print(f"{self.name} is sick from infection!")
            if random.randint(0,level) == 0:
                self.current_status = "Filthy"
            else:
                print(f"{self.name} has died from his infections...")
                self.current_status = "Dead"
            self.dirtiness = 10
        self.hunger += random.randint(1,level)
        if self.hunger > 10:
            print(f"{self.name} has died of starvation")
            self.current_status = "Dead"
            self.hunger = 10
    #Method to print pet stats
    def print_pet_stats(self):
        print(f"\nCreature Name: {self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Boredom (0-10): {self.boredom}")
        print(f"Tiredness (0-10): {self.tiredness}")
        print(f"Dirtiness (0-10): {self.dirtiness}")

        print(f"\nFood Inventory: {self.food_inventory} pieces")
        print(f"Current Status: {self.current_status}")
    #Method to feed pet
    def eat(self, level):
        if self.food_inventory == 0:
            print("Sorry, you do not have enough food to feed your pet.")
        elif self.hunger == 0:
            print(f"{self.name} is not hungry at the moment.")
        else:
            self.food_inventory -= 1
            self.hunger -= 5 + random.randint(1,3) - level
            print(f"Yumm! {self.name} ate a great meal!")
            if self.hunger < 0:
                self.hunger = 0
    #Method to play with pet
    def play(self, level):
        #Guessing game, if won, pet loses a lot more boredom
        print(f"\n{self.name} wants to play a game.")
        print(f"{self.name} is thinking of a number 0, 1, or 2")
        random_num = random.randint(0,2)
        guess = int(input("What is your guess: "))
        if guess == random_num:
            print("That is correct!!!")
            self.boredom -= 8 + random.randint(1,3) - level
        else:
            print("That is incorrect")
            self.boredom -= 6 + random.randint(1,3) - level
        if self.boredom < 0:
            self.boredom = 0
    #Method to make pet sleep
    def sleep(self, level):
        if self.tiredness == 0:
            print(f"Sorry, {self.name} doesn't want to sleep right now")
        else:
            print("Zzzzzz...Zzzzzz...Zzzzzz...")
            self.tiredness -= 5 + random.randint(1,3) - level
            if self.tiredness < 0:
                self.tiredness = 0
    #Method to clean pet
    def wash(self):
        if self.dirtiness == 0:
            print(f"Sorry, {self.name} doesn't want to take a bath")
        else:
            print(f"{self.name} took a nice long bath!")
            self.dirtiness = 0
    #Method to collect food
    def collect_food(self, level):
        collected_food = 5 + random.randint(1,3) - level
        print(f"You went foraging and found {collected_food} pieces of food")
        self.food_inventory += collected_food


#Function to retrieve player input given pet is awake
def get_awake_action():
    print("\nEnter (1) to eat.\nEnter (2) to play.\nEnter (3) to sleep.\nEnter (4) to take a bath.\nEnter (5) to forage for food.")
    response = int(input("What is your choice: "))
    if response in range(1,6):
        return response
    else:
        return False
#Main program loop
while True:
    #Welcome message
    print("Welcome to the Pythonagachi Simulator App")
    #Select game difficulty
    difficulty = int(input("Please choose a difficulty level: "))
    #Select pet name
    pet_name = input("What name would you like to give your pet Pythonagachi: ").title().strip()

    #Initialise player pet
    user_pet = Pet(difficulty, pet_name)

    #Initialise round counter
    round = 0

    #Game loop
    while True:
        #Increment round
        round += 1

        print("\n----------------------------------------------------------------------------")
        print(f"Round #{round}")

        #Print pet statistics pre-action
        user_pet.print_pet_stats()

        #Prompt user input based on pet's current status
        if user_pet.current_status == "Awake" or user_pet.current_status == "Filthy":
            choice = get_awake_action()

        if user_pet.current_status == "Bored":
            print("\n")
            choice == 2
        
        if user_pet.current_status == "Asleep":
            print("\n")
            choice == 3

        #Activate function based off choice.
        if choice == 1:
            user_pet.eat(difficulty)
        elif choice == 2:
            user_pet.play(difficulty)
        elif choice == 3:
            user_pet.sleep(difficulty)
        elif choice == 4:
            user_pet.wash()
        elif choice == 5:
            user_pet.collect_food(difficulty)
        else:
            print("Please choose a valid option")
        
        #Print pet statistics post-action
        print(f"\n Round {round} Summary:")
        user_pet.print_pet_stats()

        #Prompt user input to continue to next loop
        input("\nPress (enter) to continue")

        #Update pet statistics based on difficulty
        user_pet.update_stats(difficulty)

        #Check if pet is dead, if so end game
        if user_pet.current_status == "Dead":
            print("\nR.I.P.")
            print(f"{user_pet.name} has survived a total of {round} rounds.")
            play_again = input("Would you like to play again (y/n): ").lower().strip()
            if play_again == "y":
                break
            else:
                print("Thank you for playing Pythonagachi!")
                quit()
