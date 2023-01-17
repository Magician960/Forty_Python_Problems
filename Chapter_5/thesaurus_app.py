#You are responsible for writing a program that simulates a thesaurus. Your program will present
#a user with a list of words that your thesaurus contains. Based on the users choice, you will
#randomly present them with a synonym for their chosen word. Lastly, your program will display
#all of the potential synonyms for each word in the thesaurus.

#Initialise required libraries
import random

#Welcome message
print("Welcome to the Thesaurus App!\n\nChoose a word from the thesaurus and I will give you a synonym")

#Initialise thesaurus
thesaurus = {
    "hot":["balmy","summery","tropical","boiling","scorching"],
    "cold":["chilly","cool","freezing","frigid","polar"],
    "happy":["content","cheery","merry","jovial","jocular"],
    "sad":["unhappy","downcast","miserable","glum","melacholy"]
}

#Display possible user choices
print("\nHere are the words in the thesaurus:")
for word in thesaurus.keys():
    print(f"\t-{word}")

#Ask for user input
user_word = input("What word would you like a synonym for: ").lower()

#Display one synonym
print(f"A synonym for {user_word} is {thesaurus[user_word][random.randint(0,4)]}.")

#Ask to display entire thesaurus
user_choice = input("\nWould you like to see the whole thesaurus (yes/no): ").lower()

if user_choice == "yes":
    for word in thesaurus.keys():
        print(f"\n{word.title()} synonyms are:")
        for synonym in thesaurus[word]:
            print(f"\t-{synonym}")
elif user_choice == "no":
    print("\nI hope you enjoyed the program. Thank you!")