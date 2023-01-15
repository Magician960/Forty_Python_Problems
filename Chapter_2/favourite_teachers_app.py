#You are responsible for writing a program that will create a list of a user’s favorite teachers. It
#will display these teachers ranked (assuming the first teacher entered is the favorite, the second
#teacher entered is the next favorite, ect…), alphabetically, in reverse alphabetical order, the top
#two teachers, the next two teachers, the last favorite teacher, and the total number of favorite
#teachers in the list. Your program will then add and remove teachers from this list, each time
#displaying a similar summary.

#Teacher summary function

def summary(list):
    print(f"\nYour favourite teachers ranked are: {list}")
    print(f"Your favourite teachers alphabetically are: {sorted(list)}")
    print(f"Your favourite teachers in reverse alphabetical order are: {sorted(list, reverse=True)}")

    print(f"\nYour top two teachers are: {list[0]} and {list[1]}.")
    print(f"Your next two teachers are: {list[2]} and {list[3]}.")
    print(f"Your last favourite teacher is: {list[-1]}.")
    print(f"You have a total of {len(list)} favourite teachers.")

#Initialise list
teachers = []

#Welcome message
print("Welcome to the Favourite Teachers Program")

#Ask for user's favourite teachers
teachers.append(input("\nWho is your first favourite teacher: ").title().strip())
teachers.append(input("Who is your second favourite teacher: ").title().strip())
teachers.append(input("Who is your third favourite teacher: ").title().strip())
teachers.append(input("Who is your fourth favourite teacher: ").title().strip())

#Initial summary
summary(teachers)

#Ask user for new first favourite teacher
teachers.insert(0, input(f"\nOops, {teachers[0]} is no longer your first favourite teacher. Who is your new FAVOURITE teacher: ").title().strip())

#Second summary
summary(teachers)

#Ask user to remove a teacher
teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title().strip())

#Final summary
summary(teachers)