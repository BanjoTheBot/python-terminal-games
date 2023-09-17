"""
Lachlan Paul, 2023
Simulates a game of hangman, with custom input or words from a predetermined list
"""

def main():
    while True:
        mode = input("\nWould you like to input a custom word, or have one picked for you? Y/N ").lower().strip()
        if mode == "y":
            print("place")
        elif mode == "n":
            print("place")
        else:
            print("\nPlease input Y or N for yes or no")
            continue

if __name__ == "__main__":
    main()