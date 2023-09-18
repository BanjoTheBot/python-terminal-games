"""
Lachlan Paul, 2023
Simulates a game of hangman, with custom input or words from a predetermined list
"""
import random
from words import word_list

known_letters = []
letters = []
tries = 11

def main():
    while True:
        mode = input("\nY to input a custom word, N for pre-chosen word, ").lower().strip()
        try:
            word = choose_word(mode)
            break
        except ValueError:
            print("\nPlease input Y or N for yes or no")
            continue

    for i in word:
        known_letters.append("_")
        letters.append(i)
    
    while True:
        print(known_letters)
        if known_letters == letters:
            print("Congrats, you win!")
        if tries == 11:
            print("You lose :(")

        guess = input("What's your guess? ")
        if guess.len() > 1:
            print("More than one letter\n")
            continue

        guess_word(guess)
    

def choose_word(selection):
    if selection == "y":
        word = random.choice(word_list)
    elif selection == "n":
        word = input("Input your word, make sure nobodies looking! ")
    else:
        raise ValueError
    
    return word

def guess_word(guess):
    for i in letters:
        if i in guess:
            known_letters.insert(i, guess)
            known_letters.remove(i)
        else:
            tries -= 1
            print(f"Wrong answer, {tries} tries remaining\n")

if __name__ == "__main__":
    main()