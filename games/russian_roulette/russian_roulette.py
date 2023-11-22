"""
    Uses randomization and a list to simulate a game of Russian Roulette
    Lachlan Paul, 2023
"""
import random

bullets = [1, 0, 0, 0, 0, 0]

while True:
    input("\nPress Enter to Begin ")
    chamber = random.choice(bullets)

    if chamber == 1:
        print("\nBANG! Your brains fly across the room! Your companions look on horrified.")
        print("What a mess...")
        break
    else:
        print("\nTheres a click, and nothing happens.")
        print("You pass the gun on, living to die another day..\n")
        bullets.remove(chamber)
