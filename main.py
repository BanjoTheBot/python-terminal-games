"""
    The main file, all games can be accessed from here
    Lachlan Paul, 2023
"""
import platform
import subprocess

# Unsure if these should be sorted by Alphabetical order or order of addition
# Will probably split up lists if I make a lot of games that can be categorized
games = {
    1: "russian_roulette",
    2: "hangman",
    3: "tic-tac-toe"
}

print("Available games to play:\n")

for game in games:
    name = games[game].title()
    name = name.replace("_", " ")
    print(f"{game}: {name}\n")

while True:
    try:
        selection = int(input("Input game number: "))
        if selection not in games:
            print("Not a Valid Number!")
        else:
            break
    except ValueError:
        print("Input a number!")

for game in games:
    if game == selection:
        script_path = f"games/{games[game]}/{games[game]}.py"

        # If the code is being run on Linux, it will use python3 as the interpreter path
        # I don't personally face this issue, I assume my distro has an alias?
        if platform.system() == "Linux":
            subprocess.run(['python3', script_path], check=True, cwd='./')
        else:
            subprocess.run(['python', script_path], check=True, cwd='./')
