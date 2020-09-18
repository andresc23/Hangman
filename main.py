# For use finditer
import re

# For clearing the screen
import os

# For using sleep function
import time



print("Welcome to Hangman in Python by Andres Cisneros")

answer_var = input("Please type in a word to have other people guess.\n")

while(not answer_var.isalpha()):
    answer_var = input("Please only type in letters for your word.\n")

print("Your word is:", answer_var)

# For keeping track and displaying player's progress.
progress_var = "_" * len(answer_var)

time.sleep(1)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

print("Now it is time for the other player to guess the word")

chances = 6

# Keep track of letters already guessed so as to not repeat them.
guessed_letters = set()

while chances != 0:
    print("Current progress:", progress_var, "\n")

    print("You have", chances, "left.\n")

    input_char_guess = input("Please type in a character to guess the other person's word.\n")

    if((len(input_char_guess) != 1) or (input_char_guess.isalpha() == False)):
        print("Please only type in 1 letter, and only 1 letter at a time.\n")

    else:
        if(input_char_guess in guessed_letters):
            print("That letter has already been guessed, please guess another.\n")

        # Record newly-guessed letters and both their uppercase and lowercase versions.
        elif(input_char_guess not in guessed_letters):
            guessed_letters.add(input_char_guess)
            guessed_letters.add(input_char_guess.upper())
            guessed_letters.add(input_char_guess.lower())

            if(input_char_guess in answer_var or input_char_guess.upper() in answer_var or input_char_guess.lower() in answer_var):
                print("You have guessed correctly.\n")

                # Find indeces of where characters match. Then replace the letters in progress_var.
                # Could use a function here, but currently giving errors when I try to do so.
                matches_pos = [i.start() for i in re.finditer(input_char_guess, answer_var)]
                matches_pos = [int(i) for i in matches_pos]
                for x in matches_pos:
                    progress_var = progress_var[:x] + input_char_guess + progress_var[x+1:]

                matches_pos = [i.start() for i in re.finditer(input_char_guess.upper(), answer_var)]
                matches_pos = [int(i) for i in matches_pos]
                for x in matches_pos:         
                    progress_var = progress_var[:x] + input_char_guess.upper() + progress_var[x+1:]

                matches_pos = [i.start() for i in re.finditer(input_char_guess.lower(), answer_var)]
                matches_pos = [int(i) for i in matches_pos]
                for x in matches_pos:         
                    progress_var = progress_var[:x] + input_char_guess.lower() + progress_var[x+1:]

            else:
                print("You have guessed incorrectly.\n")
                chances = chances - 1
    if(chances == 0):
        print("You are out of chances. Game Over!")
        break

    if(progress_var == answer_var):
        print("The answer was:", answer_var, "\nYou guessed the word. Congratulations!")
        break
