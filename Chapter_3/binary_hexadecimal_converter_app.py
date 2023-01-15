#You are responsible for writing a program that will generate binary and hexadecimal values from
#1 up to a specified user value. Recall that decimal is a base 10 number system, binary is a
#base 2 number system, and hexadecimal is a base 16 number system. Your program will use
#list slicing to first only show a portion of these values. Your program will then loop through the
#entire lists of decimal, binary, and hexadecimal values to show the relationship between
#numbers of different bases.

#Welcome message
print("Welcome to the Binary/Hexadecimal Converter App")

#Function to print lists
def print_list(list):
    for num in list[slice_start - 1:slice_end]:
        print(num)

#Create lists up til user inputted number
decimal_list = list(range(1, int(input("\nCompute binary and hexadecimal values up to the following decimal number: ")) +1))
binary_list = [bin(num) for num in decimal_list]
hexadecimal_list = [hex(num) for num in decimal_list]
print("Generating lists...complete!")

#Ask user for slice start/end
print("\nUsing slices, we will now show a portion of each list.")
slice_start = int(input("What decimal number would you like to start at: ")) 
slice_end = int(input("What decimal number would you like to stop at: "))

#Print sliced lists
print(f"\nDecimal values from {slice_start} to {slice_end}:")
print_list(decimal_list)

print(f"\nBinary values from {slice_start} to {slice_end}:")
print_list(binary_list)

print(f"\nHexadecimal values from {slice_start} to {slice_end}:")
print_list(hexadecimal_list)

#Press enter to print all list values
input(f"\nPress Enter to see all values from {decimal_list[0]} to {decimal_list[-1]}.")
print("Decimal----Binary----Hexadecimal\n----------------------------------------------------------")

for dec, bin, hex in zip(decimal_list,binary_list,hexadecimal_list):
    print(f"{dec}----{bin}----{hex}")
