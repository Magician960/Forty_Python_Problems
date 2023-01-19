#You are responsible for writing a program that plays a word guessing game with a user. Your
#program will provide a category of words to the user and a string of dashes “-----” that represent
#the length of the word. The user will guess the word and with each incorrect guess, your
#program will reveal a letter at random, “-a---”. Upon guessing the word correctly, your program
#will then inform the user how many guesses they took.

import random

#Print Welcome message
print("Welcome to the Guess My Word App")

#Initialise game dictionary
game_dict = {
    "Country": ["Australia","Japan","Korea","China","Russia","USA"],
    "Stray Kids Member": ["Chan","Minho","Han","Hyunjin","Changbin","Felix","Seungmin","Jeongin"],
    "Video Games": ["Minecraft","Overwatch","Skyrim","Hades","Oblivion","Journey"]
}

#Initialise game flag
game_flag = True

#Game loop
while game_flag:
    #Randomly select category and word for game
    category = random.choice(list(game_dict.keys()))

    word = random.choice(game_dict[category])

    #Initialise list of letters of word and placeholders
    letters_word = [letter for letter in word]
    placeholder = ["-" for letter in letters_word]

    #Print question
    print(f"\nGuess a {len(word)} letter word from the following category: {category}")
    for i in placeholder:
        print(i, end="")

    #Round loop
    guess = ""
    guess_count = 0

    while guess != word:
        guess_count += 1
        guess = input("\n\nEnter your guess: ").title().strip()
        if guess != word:
            #Replace one "-" with correct letter
            print("That is not correct. Let us reveal a letter to help you!")
            #Initialise flag for while loop
            flag = True
            while flag:
                random_index = random.randint(0, len(word) - 1)
                if placeholder[random_index] == "-":
                    placeholder[random_index] = letters_word[random_index]
                    flag = False
                elif placeholder == letters_word:
                    print("You should know the answer by now...")
                    flag = False
            for i in placeholder:
                print(i, end="")

    print(f"\nCorrect! You guessed the word in {guess_count} guesses.")
    response = input("Would you like to play again (y/n): ").lower().strip()
    if response != "y":
        game_flag = False

#Ending message
print("\nThank you for playing our game!")



