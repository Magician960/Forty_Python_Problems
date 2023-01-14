#You are responsible for writing a program that will get a message and a specific letter from a
#user and then count the number of occurrences of that letter in the given message. Your
#program should count “H” and “h” as an occurence of h. Your program will then display a
#message to the user stating the occurrences of the given letter.

#Print introductory message
print("Welcome to the Letter Counter App")

#Ask for user's name
name = input("What is your name:").title()

#Greets user and introduces program
print(f"Hello {name}!\nI will count the number of times that a specific letter occurs in a message.")

#Stores message and converts to lowercase
message = input("Please enter a message:").lower()

#Asks user for letter to count
letter = input("Which letter would you like to count the occurrences of:").lower()

#Counts number of letters in message
msg_count = message.count(letter)

print(f"{name}, your message has {msg_count} {letter}'s in it!")