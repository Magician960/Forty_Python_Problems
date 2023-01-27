#You will be responsible for writing a program the emulates playing the hit game Pokemon. Your
#program will generate Pykemon creatures randomly. Each Pykemon creature will be one of
#three different elemental types: fire, water, or grass. Each Pykemon type will have its own set
#of unique moves and each individual Pykemon will have it’s one name, health stat, and speed
#stat.You will be given one Pykemon and then be tasked with fighting other pykemon until you
#run out of health. In the original Pokemon, the user is presented with three Pokemon to choose
#from at the start of the game; one of each elemental type. Pykemon is no different. You will
#choose your starting Pykemon and then be off on a journey to battle other wild Pykemon until
#your Pykemon faints.

#Import required libraries
import random

##CLASSES

#Parent class for Pykemon
class Pykemon():
    def __init__(self, name, element, health, speed):
        self.name = name
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    #Method for light attack
    def light_attack(self, enemy_pykemon):
        #Generate random damage for move
        damage = random.randint(15,25)
        #Print move
        print(f"{self.name} used {self.moves[0]}")
        print(f"{self.name} dealt {damage} damage!")
        #Subtract damage from enemy pykemon's health
        enemy_pykemon.current_health -= damage
    
    #Method for heavy attack
    def heavy_attack(self, enemy_pykemon):
        #Generate random damage for move
        damage = random.randint(0,50)
        #Print move
        print(f"{self.name} used {self.moves[1]}")
        #Determine whether the move will hit
        if damage < 10:
            print("The attack missed")
        else:
            print(f"{self.name} dealt {damage} damage!")
            #Subtract damage from enemy pykemon's health
            enemy_pykemon.current_health -= damage
    
    #Method for restorative move
    def restore(self):
        #Generate random healing amount
        heal = random.randint(15,25)
        #Print move
        print(f"{self.name} used {self.moves[2]}")
        print(f"{self.name} healed {heal} HP!")
        #Add heal amount to current health
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    #Method for check for fainting conditions
    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print(f"{self.name} has fainted...")
            input("Press Enter to continue.")

    #Method to display Pykemon stats
    def show_stats(self):
        print(f"\nName: {self.name}")
        print(f"Element Type: {self.element}")
        print(f"Health: {self.current_health} / {self.max_health}")
        print(f"Speed: {self.speed}")

#Child class for water-type Pykemon
class Water_pykemon(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Bite","Splash","Dive","Water Cannon"]
    
    #Method for special attack
    def special_attack(self, enemy_pykemon):
        print(f"{self.name} used {self.moves[3]}")
        #Generate damage based off enemy pykemon's attribute
        if enemy_pykemon.element == "FIRE":
            print("The move is super effective!")
            damage = random.randint(35,50)
        elif enemy_pykemon.element == "GRASS":
            print("The move is not very effective")
            damage = random.randint(5,10)
        else:
            damage = random.randint(10,20)
        print(f"{self.name} dealt {damage} damage!")
        #Subtract enemy pykemon's health based off damage
        enemy_pykemon.current_health -= damage
    
    #Method to print moves
    def move_info(self):
        print(f"\n{self.name} Moves:")
        print(f"--{self.moves[0]}--")
        print("  An efficient attack...")
        print("  Guaranteed to do damage within the range of 15 to 25 damage points.")

        print(f"\n--{self.moves[1]}--")
        print("  A risky attack...")
        print("  Could deal up to 50 damage points or as little as 0 damage points.")

        print(f"\n--{self.moves[2]}--")
        print("  A restorative move...")
        print("  Guaranteed to heal your Pykemon 15 to 25 health points")

        print(f"\n--{self.moves[3]}--")
        print(f"  A powerful {self.element} based attack...")
        print("  Guaranteed to deal MASSIVE damage to FIRE type Pykemon.")


#Child class for fire-type Pykemon
class Fire_pykemon(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Scratch", "Ember", "Light", "Fire Blast"]

    #Method for special attack
    def special_attack(self, enemy_pykemon):
        print(f"{self.name} used {self.moves[3]}")
        #Generate damage based off enemy pykemon's attribute
        if enemy_pykemon.element == "GRASS":
            print("The move is super effective!")
            damage = random.randint(35,50)
        elif enemy_pykemon.element == "WATER":
            print("The move is not very effective")
            damage = random.randint(5,10)
        else:
            damage = random.randint(10,20)
        print(f"{self.name} dealt {damage} damage!")
        #Subtract enemy pykemon's health based off damage
        enemy_pykemon.current_health -= damage

    #Method to print moves
    def move_info(self):
        print(f"\n{self.name} Moves:")
        print(f"--{self.moves[0]}--")
        print("  An efficient attack...")
        print("  Guaranteed to do damage within the range of 15 to 25 damage points.")

        print(f"\n--{self.moves[1]}--")
        print("  A risky attack...")
        print("  Could deal up to 50 damage points or as little as 0 damage points.")

        print(f"\n--{self.moves[2]}--")
        print("  A restorative move...")
        print("  Guaranteed to heal your Pykemon 15 to 25 health points")

        print(f"\n--{self.moves[3]}--")
        print(f"  A powerful {self.element} based attack...")
        print("  Guaranteed to deal MASSIVE damage to GRASS type Pykemon.")

#Child class for grass_type Pykemon
class Grass_pykemon(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]

    #Method for special attack
    def special_attack(self, enemy_pykemon):
        print(f"{self.name} used {self.moves[3]}")
        #Generate damage based off enemy pykemon's attribute
        if enemy_pykemon.element == "WATER":
            print("The move is super effective!")
            damage = random.randint(35,50)
        elif enemy_pykemon.element == "FIRE":
            print("The move is not very effective")
            damage = random.randint(5,10)
        else:
            damage = random.randint(10,20)
        print(f"{self.name} dealt {damage} damage!")
        #Subtract enemy pykemon's health based off damage
        enemy_pykemon.current_health -= damage

    #Method to print moves
    def move_info(self):
        print(f"\n{self.name} Moves:")
        print(f"--{self.moves[0]}--")
        print("  An efficient attack...")
        print("  Guaranteed to do damage within the range of 15 to 25 damage points.")

        print(f"\n--{self.moves[1]}--")
        print("  A risky attack...")
        print("  Could deal up to 50 damage points or as little as 0 damage points.")

        print(f"\n--{self.moves[2]}--")
        print("  A restorative move...")
        print("  Guaranteed to heal your Pykemon 15 to 25 health points")

        print(f"\n--{self.moves[3]}--")
        print(f"  A powerful {self.element} based attack...")
        print("  Guaranteed to deal MASSIVE damage to WATER type Pykemon.")

#Game class for game objects and functions
class Game():
    def __init__(self):
        self.pykemon_elements = ["FIRE","WATER","GRASS"]
        self.pykemon_names = ['Chewdie', 'Spatol',
                            'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot',
                            'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
        self.battles_won = 0

    #Method to print introduction to game
    def print_intro(self):
        print("Welcome to Pykemon!")
        print("Can you become the worlds greatest Pykemon Trainer???")
        print("\nDon't worry! Prof Eramo is here to help you on your quest.")
        print("He would like to gift you your first Pykemon!")
        print("Here are three potential Pykemon partners.")
        input("Press enter to choose your Pykemon!")

    #Method to generate a pykemon
    def generate_pykemon(self):
        #Generate randomised stats for pykemon
        random_health = random.randint(70,100)
        random_speed = random.randint(1,10)
        random_element = random.choice(self.pykemon_elements)
        random_name = random.choice(self.pykemon_names)
        #Generate pykemon
        if random_element == "FIRE":
            created_pykemon = Fire_pykemon(random_name, random_element, random_health, random_speed)
        elif random_element == "WATER":
            created_pykemon = Water_pykemon(random_name, random_element, random_health, random_speed)
        else:
            created_pykemon = Grass_pykemon(random_name, random_element, random_health, random_speed)

        return created_pykemon    

    #Method for user to generate and choose from 3 starter pokemon
    def choose_pykemon(self):
        starters = []
        while len(starters) < 3:
            starter_pykemon = game.generate_pykemon()
            valid_pykemon = True
            #Check that generated starter is unique
            for starter in starters:
                if starter.name == starter_pykemon.name or starter.element == starter_pykemon.element:
                    valid_pykemon = False
            #Add generated pykemon to starter list if unique
            if valid_pykemon:
                starters.append(starter_pykemon)
        
        #Print stats and moves for all starters
        for starter in starters:
            starter.show_stats()
            starter.move_info()
        
        #Print selection screen
        print("\nProfessor Eramo presents you with three Pykemon:")
        print(f"(1) - {starters[0].name}")
        print(f"(2) - {starters[1].name}")
        print(f"(3) - {starters[2].name}")
        #Retrieve user choice
        choice = int(input("Which Pykemon would you like to choose: "))
        chosen_pykemon = starters[choice - 1]
        #Print chosen pykemon
        print(f"\nCongratulations Trainer, you have chosen {chosen_pykemon.name}")
        input(f"\nYour journey with {chosen_pykemon.name} begins now...Press Enter")
        
        return chosen_pykemon
    
    #Method to get player's attack choice
    def get_attack(self, pykemon):
        #Print out moves
        print("\nWhat would you like to do...")
        print(f"(1) - {pykemon.moves[0]}")
        print(f"(2) - {pykemon.moves[1]}")
        print(f"(3) - {pykemon.moves[2]}")
        print(f"(4) - {pykemon.moves[3]}")
        #Get user's move
        move = int(input("Please enter your move choice: "))

        #Formatting
        print("")
        print("------------------------------------------")

        return move

    #Method for player attacking
    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)
        #Check if computer's pykemon has fainted
        computer.faint()

    #Method for computer attacking
    def computer_attack(self, player, computer):
        move = random.randint(1,4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)
        #Check if player's pykemon has fainted
        player.faint()

    #Method to simulate battle
    def battle(self, player, computer):
        #Collect user's attack
        attack = game.get_attack(player)
        #If user pykemon is faster than computer's, user goes first
        if player.speed >= computer.speed:
            game.player_attack(attack, player, computer)
            if computer.is_alive:
                game.computer_attack(player, computer)
        else:
            game.computer_attack(player, computer)
            if player.is_alive:
                game.player_attack(attack, player, computer)




##MAIN PROGRAM LOOP
while True:

    #Initialise game object
    game = Game()

    #Print introductory message
    game.print_intro()

    #Get user to pick their starter pykemon
    user_pykemon = game.choose_pykemon()

    #game loop
    while user_pykemon.is_alive:
        #Generate computer's pykemon and print stats
        opponent_pykemon = game.generate_pykemon()
        print(f"\nOH NO! A wild {opponent_pykemon.name} has appeared!")
        opponent_pykemon.show_stats()
        
        #Battle loop
        while user_pykemon.is_alive and opponent_pykemon.is_alive:
            game.battle(user_pykemon, opponent_pykemon)
            #Print stats for both if both alive
            if user_pykemon.is_alive and opponent_pykemon.is_alive:
                user_pykemon.show_stats()
                opponent_pykemon.show_stats()
                print("--------------------------------------------------------------------------------")
        if user_pykemon.is_alive:
            game.battles_won += 1

    print(f"\n{user_pykemon.name} has fainted...")
    print(f"You have defeated {game.battles_won} pykemon")

    #Get user input whether to play again
    play_again = input("Would you like to play again(y/n): ").lower().strip()

    #Quit game if they wish
    if play_again != "y":
        print("\nThank you for playing!")
        quit()