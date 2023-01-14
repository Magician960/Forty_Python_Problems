#You are responsible for writing a program that will collect four grades from a user. Your
#program will then sort these grades from highest to lowest. Then, your program will simulate
#dropping the lowest two grades the user entered. Lastly, it will comment on the users highest
#grade.

grades = []

print("Welcome to the Grade Sorter App")

grades.append(int(input("\nWhat is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

print(f"\nYour grades are: {grades}")

grades.sort(reverse = True)

print(f"\nYour grades from highest to lowest are: {grades}")

print("\nThe lowest two grades will now be dropped.")

print(f"Removed grade: {grades.pop()}")
print(f"Removed grade: {grades.pop()}")

print(f"\nYour remaining grades are: {grades}\nNice Work! Your highest grade is a {grades[0]}.")
