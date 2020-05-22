# The continue statement - the Ugly Vowel Eater
# ------------------------
# Scenario
# ----------------
# The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
# It can be used with both the while and for loops.
# task is very special: you must design a vowel eater! Write a program that uses :
    # a for loop;
    # the concept of conditional execution (if-elif-else)
    # the continue statement.

    # Your program must :
        # ask the user to enter a word;
        # use userWord = userWord.upper() to convert the word entered by the user to upper case; 
        #     we'll talk about the so-called string methods and the upper() method very soon - don't worry;
        # use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
        # print the uneaten letters to the screen, each one of them on a separate line.

# Prompt the user to enter a word
# and assign it to the userWord variable.
userword = input("enter the letter : ")
userword = userword.upper()

for letter in userword:
    # Complete the body of the for loop.
        if letter == 'A' :
            continue
        elif letter == 'I' :
            continue
        elif letter == 'U' :
            continue
        elif letter == 'E' :
            continue
        elif letter == 'O' :
            continue
        else :
            print(letter)