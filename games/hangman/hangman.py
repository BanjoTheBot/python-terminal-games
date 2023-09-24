"""
Lachlan Paul, 2023
Simulates a game of hangman, with custom input or words from a predetermined list
"""
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from words import word_list

colorama_init()

wrong_letters = []
known_letters = []
letters = []
tries = 11

def main():
    while True:
        mode = input("\nY to input a custom word, N for pre-chosen word, ").lower().strip()

        # The ‘\033’ is the escape character
        # The ‘[1A’ says go up one line and the ‘[K’ says erase to the end of this line.
        # Apparently this won't work on all terminals? I hope there are no issues...
        print ('\033[1A' + '\033[K')

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
            print(f"{Fore.GREEN}Congrats, you win!{Style.RESET_ALL}")
            break
        if tries == 0:
            print(f"\n{Fore.RED}You lose :({Style.RESET_ALL}")
            print(f"The word was {Fore.GREEN}{''.join(word)}{Style.RESET_ALL}")
            break

        print("\nLetters you've already tried:")
        print(wrong_letters)
        guess = input("What's your guess? ").lower().strip()
        # This is here so that the input is still on the same line, but there's a space after the input
        print("\n")
        
        if len(guess) > 1:
            print(f"{Fore.RED}More than one letter{Style.RESET_ALL}\n")
            continue
        elif len(guess) == 0:
            continue
        elif guess in wrong_letters or guess in known_letters:
            print(f"\n{Fore.RED}You've already tried that letter{Style.RESET_ALL}\n")
            continue

        guess_word(guess)

def choose_word(selection):
    if selection == "y":
        word = input("Input your word, make sure nobodies looking! ").lower().strip()
        print ('\033[1A' + '\033[K')
        word = list(word)
    elif selection == "n":
        word = random.choice(word_list)
    else:
        raise ValueError
    
    return word

def guess_word(guess):
    global tries
    it_is_found = False

    for index, item in enumerate(letters):
        if item == guess:
            known_letters[index] = guess
            it_is_found = True

    if it_is_found is True:
        it_is_found = False
    else:
        tries -= 1
        wrong_letters.append(guess)
        print(f"\n{Fore.RED}Wrong answer, {tries} tries remaining{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
