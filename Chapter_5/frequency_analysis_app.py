#You are responsible for writing a program that will analyse the letter distribution of a given text.
#Your program will take any text, remove all non-alpha characters, count the frequency of each
#letter within the text, calculate the percentage of occurrence for each letter, and create a list of
#letters ordered from highest occurrence to lowest occurrence. Your program will perform these
#operations for two different bodies of text.

#Initialise required libraries
from collections import Counter

#Welcome message
print("Welcome to the Frequency Analysis App")

#Frequency analysis function
def freq_analysis(string):
    for letter in string_list:
        if letter not in letter_frequency.keys():
            letter_frequency[letter] = 1
        else:
            letter_frequency[letter] += 1

for i in range(1,3):
    #Initialise dictionary
    letter_frequency = {}

    #Collect user string
    raw_string = input("\nEnter a word or phrase to count the occurrence of each letter: ")

    #Prepare string for frequency analysis
    clean_string = "".join(filter(str.isalpha, raw_string.lower().strip()))
    string_list = list(clean_string)

    #Conduct frequency analysis
    freq_analysis(string_list)
    total_frequency = sum(letter_frequency.values())

    #Print frequency analysis table
    print(f"\nHere is the frequency analysis from key phrase {i}:")
    print("\n\tLetter\tOccurrence\tPercentage")
    #Sort dictionary alphabetically
    letter_frequency_letter = dict(sorted(letter_frequency.items()))
    for letter, frequency in letter_frequency_letter.items():
        percentage = round(frequency/total_frequency*100, 2)
        print(f"\t{letter}\t{frequency}\t\t{percentage}%")
    
    ###My method
    print("\nLetters ordered from highest occurrence to lowest:")
    #Sort dictionary by highest occurrence to lowest
    letter_frequency_number = dict(sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True))
    #Hold sorted letters in temporary list
    holding_list = []
    for i in letter_frequency_number.keys():
        holding_list.append(i)
    #Create ordered letter string to print
    ordered_string = ''.join(holding_list)
    print(ordered_string)

    ###Instructor's solution; whilst both sort from highest occurrence, for letters with same no. of occurences, order differs
    #letter_count = Counter(clean_string)
    ##Make a list of letters from highest occurrence to lowest
    #ordered_letter_count = letter_count.most_common()
    #clean_string_ordered_letters = []
    #for pair in ordered_letter_count:
    #    clean_string_ordered_letters.append(pair[0])

    ##Print the list
    #print("\nLetters ordered from highest occurrence to lowest: ")
    #for letter in clean_string_ordered_letters:
    #   print(letter, end='')