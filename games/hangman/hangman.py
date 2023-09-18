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
        if tries == 0:
            print("You lose :(")
            print(f"The word was {word}")
            break

        guess = input("What's your guess? ").lower().strip()
        if len(guess) > 1:
            print("More than one letter\n")
            continue

        guess_word(guess)
    

def choose_word(selection):
    if selection == "y":
        word = input("Input your word, make sure nobodies looking! ").lower().strip()
    elif selection == "n":
        word = random.choice(word_list)
    else:
        raise ValueError
    
    return word

def guess_word(guess):
    global tries

    for i in letters:
        if i == guess:
            known_letters[i] = guess
        else:
            break

    tries -= 1
    print(f"Wrong answer, {tries} tries remaining\n")

if __name__ == "__main__":
    main()