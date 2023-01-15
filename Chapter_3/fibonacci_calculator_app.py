#You are responsible for writing a program that will compute the first n terms of the Fibonacci
#Sequence. Your program will then display these terms. Next, your program will calculate the
#ratios of consecutive Fibonacci numbers to prove that these ratios approach the irrational
#mathematical constant of Phi; 1.618….

#Welcome message
print("Welcome to the Fibonacci Calculator App")

#Ask user for number of fibonacci sequence to compute to
seq_num = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute: "))

#Initialise fibonacci sequence list
seq_list = [0,1]
golden_list = []
#Fill out seq_list
for num in range(1, seq_num):
    seq_list.append(seq_list[-1] + seq_list[-2])

#fill out golden_ratio_list
for num in range(1, seq_num + 1):
    if num == 1:
        golden_list.append(1.0)
    else:
        golden_list.append(seq_list[num] / seq_list[num - 1])

#Print out lists
print(f"\nThe first {seq_num} numbers of the Fibonacci sequence are:")
for fib in seq_list[1:]:
    print(fib)

if seq_num == 1:
    print("\nThe corresponding Golden Ratio values are:\nN/A")
else:
    print("\nThe corresponding Golden Ratio values are:")
    for ratio in golden_list[1:]:
        print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")