title = "Lizard Spock"

moves_map = {
    "1": "rock",
    "2": "paper",
    "3": "scissors",
    "4": "lizard",
    "5": "spock"
}

character_map = {
    "1": "Leonard", "2": "Amy", "3": "Raj", "4": "Bernadette",
    "5": "Penny", "6": "Stuart", "7": "Howard",
    "8": "Leslie", "9": "Professor Proton"
}

win_lose_combos = [
    ("1", "3"),  # rock vs. scissors
    ("1", "4"),  # rock vs. lizard
    ("4", "5"),  # lizard vs. spock
    ("4", "2"),  # lizard vs. paper
    ("5", "3"),  # spock vs. scissors
    ("5", "1"),  # spock vs. rock
    ("3", "2"),  # scissors vs. paper
    ("3", "4"),  # scissors vs. lizard
    ("2", "1"),  # paper vs. rock
    ("2", "5")   # paper vs. spock
]

actions = (
    "crushes",      # rock crushes scissors
    "crushes",      # rock crushes lizard
    "poisons",      # lizard poisons spock
    "eats",         # lizard eats paper
    "vaporizes",    # spock vaporizes scissors
    "vaporizes",    # spock vaporizes rock
    "smashes",      # scissors smashes paper
    "decapitates",  # scissors decapitates lizard
    "covers",       # paper covers rock
    "disproves"     # paper disproves spock
)

points_to_win = 3

scoreboard_width = 52
win_board_width = 26
