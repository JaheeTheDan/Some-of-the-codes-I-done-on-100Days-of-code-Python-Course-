'''A game of hangman. Player start with 6 lives and everytime player guess wrong letter
they loses a life. The goal is to guess the correct word and have there lifes  remaining'''
import os
import random
from hangman_words import word_list
from hangman_art import logo,stages

#A word is randomly pick from word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed_list = []

# 'cls' is used to clear screen in terminal
os.system('cls')
print(logo)
display = []

#Populate the display with '-' characters
for _ in range(word_length):
    display += "_"

while True:
    print(stages[lives])
    print('\n', ''.join(display))
    print(chosen_word)
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    #Check if the guess letter only have 1 letter and no other values
    if len(guess)>1 or guess in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        print('Your guess contain invalued text. One letter at a time')
    else:

    #Check if the letter was guessed already
        if guess in guessed_list:
            if guess not in chosen_word:
                #Tell player that guess has wrong but already guessed
                print('That guess was wrong.')
                print('And also you already guess the letter \'',guess,'\'')

            else:
                #Tell player that guess has right but already guessed
                print('That guess was right but you already guess the letter \'',guess,'\'')

        else:
            guessed_list.append(guess)# Add the guess letter to list of guesses made

            #Replace the '-' in display with the correct letter
            for position in range(word_length):
                if guess == chosen_word[position]:
                    display[position] = guess

            #Check if the guess letter is in the chosen word
            if guess in chosen_word:
                print('You have guess correctly.')

                #Check if all letter in chosen word is guessed
                if '_' not in display:
                    print('Good job. You have won.')
                    break

            else:
                lives -= 1
                print(f'You guess wrong, you have {lives} number of life left.')

                #Check if all lives are lost
                if lives == 0:
                    print('You are out of live.\nYou have lost')
                    print(f'The the word to guess was {chosen_word}')
                    break
