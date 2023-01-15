#You are responsible for writing a program that will highlight the similarities and differences
#between four different types of lists: a list of strings, a list of integers, a list of floats, and a list of
#lists. For each list, your program will describe the data type of the list, the elements of the list,
#and the data type of the first element in the list. Your program will then highlight the similarities
#and differences between sorting a list numerically and alphabetically.


#Used to return variable name of list
def get_variable_name(variable):
    globals_dict = globals()

    return [var_name for var_name in globals_dict if globals_dict[var_name] is variable]

#Used to print summary of list
def summary(list):
    print(f"\nThe variable {get_variable_name(list)[0]} is a {type(list)}\nIt contains the elements {list}\nThe element {list[0]} is a {type(list[0])}")

#Print title
print("\t\tSummary Table")

#Initialise lists
num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

list_of_lists = [num_strings,num_ints,num_floats,num_lists]

#Print summary of all lists
for list in list_of_lists:
    summary(list)

print(f"\nNow sorting num_strings and num_ints...\nSorted num_strings: {sorted(num_strings)}\nSorted num_ints: {sorted(num_ints)}")

print("\nStrings are sorted alphabetically while integers are sorted numerically!")

