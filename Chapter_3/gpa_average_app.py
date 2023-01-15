#You are responsible for writing a program that will collect any number of grades from a user.
#Your program will sort these grades numerically from highest to lowest and calculate the grade
#point average of the user. Your program will then ask for the average the user desires and
#calculate what the user must get on their next assignment to achieve this average. Lastly, your
#program will make a copy of the users grades and allow them to alter one of their previous
#grades to see how doing worse or better on an assignment would have changed their overall
#average.

#Grade Summary Function
gpa_average = []

def summary(grade_list):
    print(f"\tTotal Number of Grades: {len(grade_list)}")
    print(f"\tHighest Grade: {max(grade_list)}")
    print(f"\tLowest Grade: {min(grade_list)}")
    print(f"\tAverage: {round(sum(grade_list)/len(grade_list),2)}")
    gpa_average.append(sum(grade_list)/len(grade_list))

#Welcome message
print("Welcome to the GPA Average Calculator App")

#Collect user's name
name = input("\nWhat is your name: ").title().strip()

#Collect user's grade and add to list
grades = []

no_of_grades = int(input("How many grades would you like to enter: "))

for i in range(0, no_of_grades):
    grades.append(int(input("Enter grade: ")))

#Print grades sorted
grades.sort(reverse = True)
print("\nGrades Highest to Lowest:")

for grade in grades:
    print(f"\t{grade}")

#Print grade summary
print(f"\n{name}'s Grade Summary:")
summary(grades)

#Ask for user's desired gpa average and calculate required new grade
desired_average = float(input("\nWhat is your desired average: "))

print(f"\nGood luck {name}!\nYou will need a {desired_average*(len(grades)+1) - sum(grades)} on your next assignment to earn a {desired_average} average.")

#Ask user for grade to change
print("\nLet's see what your average could have been if you did better/worse on an assignment.")
old_grade = int(input("What grade would you like to change: "))
new_grade = int(input(f"What grade would you like to change {old_grade} to: "))

#Replace old_grade with new_grade in new_grades
new_grades = grades.copy()
new_grades.remove(old_grade)
new_grades.append(new_grade)


#Print new grades sorted
new_grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest:")

for grade in new_grades:
    print(f"\t{grade}")

#Print new grade summary
print(f"\n{name}'s New Grade Summary:")
summary(new_grades)

#Print gpa comparison
print(f"\nYour new average would be a {round(gpa_average[1],2)} compared to your real average of {round(gpa_average[0],2)}!")
print(f"That is a change of {round(gpa_average[1] - gpa_average[0], 2)} points!")

#Ending retort
print(f"\nToo bad your original grades are still the same!\n{grades}")
print("You should go ask for extra credit!")