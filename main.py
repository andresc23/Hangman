import re

print("Welcome to Hangman in Python by Andres Cisneros")

answer_var = input("Please type in a word to have other people guess.\n")

print("Your word is:", answer_var)

word_length = len(answer_var)

print(answer_var, "is", word_length, "characters long.")

progress_var = "_" * word_length

print("Now it is time for the other player to guess the word")

chances = 6

guessed_letters = set()

while chances != 0:
    print("Current progress:", progress_var, "\n")

    print("You have", chances, "left.\n")

    input_char_guess = input("Please type in a character to guess the other person's word.\n")

    if(len(input_char_guess)) != 1:
        print("Please only type in 1 letter at a time.\n")

    else:
        if(input_char_guess in guessed_letters):
            print("That letter has already been guessed, please guess another.\n")

        elif(input_char_guess not in guessed_letters):
            guessed_letters.add(input_char_guess)

            if(input_char_guess in answer_var):
                print("You have guessed correctly.\n")
                matches_pos = [i.start() for i in re.finditer(input_char_guess, answer_var)]
                matches_pos = [int(i) for i in matches_pos]
                for x in matches_pos:         
                    progress_var = progress_var[:x] + input_char_guess + progress_var[x+1:]

            else:
                print("You have guessed incorrectly.\n")
                chances = chances - 1
    if(chances == 0):
        print("You are out of chances. Game Over!")
        break

    if(progress_var == answer_var):
        print("The answer was:", answer_var, "\nYou guessed the word. Congratulations!")
        break