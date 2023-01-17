#You are responsible for writing a program that will encode or decode a message based off the
#letter distribution of a predetermined key text. Your program will determine a frequency analysis
#for two texts and use these letter distributions to create a cipher to either encode or decode a
#message based off user input. This program is an extension of the Frequency Analysis App.

#Welcome message
print("Welcome to the Code Breakers App")

#Frequency analysis function
def freq_analysis(string):
    for letter in string_list:
        if letter not in letter_frequency.keys():
            letter_frequency[letter] = 1
        else:
            letter_frequency[letter] += 1

#List to hold key phrases
key_phrase_1 = """
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any
other name.
In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any
emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably
balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the world has seen,
but as a lover he would have placed himself in a false position.
He never spoke of the softer passions, save with a gibe and a sneer.
They were admirable things for the observer excellent for drawing the veil from men's motives
and actions.
But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted
temperament was to introduce
a distracting factor which might throw a doubt upon all his mental results.
Grit in a sensitive instrument, or a crack in one of his own highpower lenses,
would not be more disturbing than a strong emotion in a nature such as his.
And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious
and questionable memory.
I had seen little of Holmes lately. My marriage had drifted us away from each other.
My own complete happiness, and the homecentred interests which rise up around the man who
first finds himself master of his own establishment,
were sufficient to absorb all my attention, while Holmes, who loathed every form of society with
his whole Bohemian soul,
remained in our lodgings in Baker Street, buried among his old books, and alternating from
week to week between cocaine and ambition,
the drowsiness of the drug, and the fierce energy of his own keen nature.
He was still, as ever, deeply attracted by the study of crime,
Page 89
and occupied his immense faculties and extraordinary powers of observation in following out
those clues,
and clearing up those mysteries which had been abandoned as hopeless by the official police.
From time to time I heard some vague account of his doings: of his summons to Odessa in the
case of the Trepoff murder,
of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee,
and finally of the mission which he had accomplished so delicately and successfully for the
reigning family of Holland.
Beyond these signs of his activity, however, which I merely shared with all the readers of the
daily press, I knew little of my former friend and companion.
 """

key_phrase_2 = """
Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I have both seen
and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling experiences, you may be
interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table.
It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very deepest moment.
Your recent services to one of the royal houses of Europe have shown that you are one who
may safely be trusted
with matters which are of an importance which can hardly be exaggerated.
This account of you we have from all quarters received.
Be in your chamber then at that hour, and do not take it amiss if your visitor wear a mask.
This is indeed a mystery, I remarked. What do you imagine that it means?
I have no data yet. It is a capital mistake to theorise before one has data.
Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
But the note itself. What do you deduce from it?
I carefully examined the writing, and the paper upon which it was written.
The man who wrote it was presumably well to do, I remarked, endeavouring to imitate my
companion's processes.
Such paper could not be bought under half a crown a packet.
It is peculiarly strong and stiff.
"""
key_phrase_list = [key_phrase_1,key_phrase_2]

#Initialise ciipher code
cipher = []

for i in range(0,2):
    #Initialise dictionary
    letter_frequency = {}

    #Collect key_phrase to analyse
    raw_string = key_phrase_list[i]

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
    for let in letter_frequency_number.keys():
        holding_list.append(let)
    #Create ordered letter string to print
    ordered_string = ''.join(holding_list)
    print(ordered_string)

    #Append to cipher list
    cipher.append(ordered_string)

code_1 = list(cipher[0])
code_2 = list(cipher[1])

#TESTING ONLY
#print(f"\n{code_1}\n{code_2}")

#Ask for user direction
encode_decode = input("Would you like to encode or decode a message: ").lower().strip()
if encode_decode == "encode":
    raw_input = input("What is the phrase: ")
    #Prepare string for encoding
    message = "".join(filter(str.isalpha, raw_input.lower().strip()))
    message = list(message)
    #Initialise list to hold encoded message letters
    encoded_letters = []
    #Encode message
    for letter_to_encode in message:
        index = code_1.index(letter_to_encode)
        encoded_letters.append(code_2[index])
    print("\nThe encoded message is:")
    for encoded_letter in encoded_letters:
        print(encoded_letter, end="")

elif encode_decode == "decode":
    encoded_message = input("What is the phrase:")
    #Prepare string for decoding
    encoded_message = list(encoded_message)
    #Initialise list to hold decoded message letters
    decoded_letters = []
    #Decode message
    for letter_to_decode in encoded_message:
        index = code_2.index(letter_to_decode)
        decoded_letters.append(code_1[index])
    print("\nThe decoded message is:")
    for decoded_letter in decoded_letters:
        print(decoded_letter, end="")


