import random
import time
import os

def choose_word():
    words = ["python","hangman","programming","computer","gaming","developer","keyboard"]
    return random.choice(words)


def display_word(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    return display


def draw_hangman(attempts_left):
    hangman_stages = [
     '''
         -----
         |   |
             |
             |
             |
             |
        ------
        ''',
        '''
         -----
         |   |
         O   |
             |
             |
             |
        ------
        ''',
        '''
         -----
         |   |
         O   |
         |   |
             |
             |
        ------
        ''',
        '''
         -----
         |   |
         O   |
        /|   |
             |
             |
        ------
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        ------
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        ------
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ------
        '''

    ]

    return hangman_stages[6 - attempts_left]
def play_sound(effect):
    print(f"Playing {effect} sound effect")


def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(draw_hangman(attempts_left))
        print("\n" + display_word(secret_word,guessed_letters))
        guess = input("Guess a letter").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter . Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
                play_sound("correct")

            else:
                print("Incorrect guess")
                attempts_left -= 1
                play_sound("Incorrect")



        else:
            print("Invalid input. Please enter a single letter.")




        if set(secret_word) <= set(guessed_letters):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(draw_hangman(attempts_left))
            print("\nCongratz!! you guessed the word" + secret_word)
            play_sound("win")
            break


        print("Attempt left:" + str(attempts_left))
        time.sleep(1)


    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(draw_hangman(attempts_left))
        print("\nSorry, you ran out of attempts. The word was:" + secret_word)
        play_sound("loose")

if __name__ == "__main__":
    hangman()

