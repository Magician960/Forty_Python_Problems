#You are responsible for writing a program that will collect four grades from a user. Your
#program will then sort these grades from highest to lowest. Then, your program will simulate
#dropping the lowest two grades the user entered. Lastly, it will comment on the users highest
#grade.

#Initialise list to hold grades
grades = []

#Introductory message
print("Welcome to the Grade Sorter App")

#Asks user for 4 grades
grades.append(int(input("\nWhat is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

#Prints grades
print(f"\nYour grades are: {grades}")

#Sorts grades in descending order
grades.sort(reverse = True)

#Shows sorted grades list
print(f"\nYour grades from highest to lowest are: {grades}")

#Drops and shows lowest two grades
print("\nThe lowest two grades will now be dropped.")

print(f"Removed grade: {grades.pop()}")
print(f"Removed grade: {grades.pop()}")

#Show remaining grades
print(f"\nYour remaining grades are: {grades}\nNice Work! Your highest grade is a {grades[0]}.")
