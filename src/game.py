import random
from util.input_checker import check_input
from util.score_tracker import get_score
import src.constants as const
import src.mutables as mut


def play_round():
    mut.sheldon_choice = random.choice(const.move)
    mut.player_choice = make_move()
    get_score()


def make_move():
    round_board = f"\nRound #{mut.round_counter}:\n"
    round_board += "{:<12}{:<12}{:<12}".format("(1) rock", "(2) paper", "(3) scissors") + "\n"
    round_board += "{:^36}".format("(4) lizard \t (5) spock")

    print(round_board)

    player_move = check_input(const.move)

    if player_move == "1" or player_move == "rock":
        return const.move[0]
    elif player_move == "2" or player_move == "paper":
        return const.move[1]
    elif player_move == "3" or player_move == "scissors":
        return const.move[2]
    elif player_move == "4" or player_move == "lizard":
        return const.move[3]
    elif player_move == "5" or player_move == "spock":
        return const.move[4]


def print_winner():
    print("\n")
    win_board = "+{}+".format("*~" * const.win_board_width) + "\n"
    win_board += ">>" + "{:^50}".format("!!! BAZINGA !!!") + "<<\n"

    if mut.player_points == const.points_to_win:
        win_board += ">>" + "{:^50}".format(f"{mut.player.title()} outsmarted Sheldon!") + "<<\n"
    else:
        win_board += ">>" + "{:^50}".format(f"Sheldon outsmarted {mut.player.title()}!") + "<<\n"

    win_board += "+{}+".format("*~" * const.win_board_width) + "\n\n"

    print(win_board)


def get_character():
    print("Choose your character: \n"
          "(1) Leonard \t (2) Amy \n"
          "(3) Raj \t\t (4) Bernadette \n"
          "(5) Penny \t\t (6) Stuart \n"
          "(7) Howard \t\t (8) Leslie \n"
          "(9) Professor Proton")

    player_name = check_input(const.character)

    if player_name == "1" or player_name == "leonard":
        return const.character[0]
    elif player_name == "2" or player_name == "amy":
        return const.character[1]
    elif player_name == "3" or player_name == "raj":
        return const.character[2]
    elif player_name == "4" or player_name == "bernadette":
        return const.character[3]
    elif player_name == "5" or player_name == "penny":
        return const.character[4]
    elif player_name == "6" or player_name == "stuart":
        return const.character[5]
    elif player_name == "7" or player_name == "howard":
        return const.character[6]
    elif player_name == "8" or player_name == "leslie":
        return const.character[7]
    elif player_name == "9" or player_name == "professor proton":
        return const.character[8]