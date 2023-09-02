"""
Lachlan Paul, 2023
Uses randomization and a list to simulate a game of Russian Roulette
"""
import random

bullets = [1, 0, 0, 0, 0, 0]

while True:
    input(f"\nPress Enter to Bargain with the Devil ")
    chamber = random.choice(bullets)

    if chamber == 1:
        print(f"\nBANG! Your brains fly across the room! Your companions look on horrified.")
        print("What a mess...")
        break
    else:
        print(f"\nTheres a click, and nothing happens.")
        print(f"You pass the gun on, living to die another day..\n")
        bullets.remove(chamber)