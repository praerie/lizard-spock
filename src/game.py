from util.input_checker import check_input
from src.const import character_map, moves_map, win_lose_combos, actions, \
    scoreboard_width, win_board_width, points_to_win


def print_round_menu(round_counter):
    round_menu = f"\nRound #{round_counter}:\n"
    for key, value in moves_map.items():
        round_menu += f"({key}) {value}\n"
    print(round_menu)


def make_move():
    player_move = check_input(moves_map)

    if player_move in moves_map.keys():
        return player_move
    
    raise InputError("Invalid input. Please enter a valid move.")


def get_round_winner(player_choice, sheldon_choice):
    if (player_choice, sheldon_choice) in win_lose_combos:
        return True
    else:
        return False


def create_scoreboard(player, player_pts, sheldon_pts, player_choice,
                      sheldon_choice, add_player_pt, add_sheldon_pt):
    board = "+{}+".format("-" * scoreboard_width) + "\n"
    board += "| " + "{:<30}{:>9}{:<1}{:>10}".format(f"{player.title()}: {player_choice}",
                                                    "+", int(add_player_pt),
                                                    f"{player_pts}") + " |\n"
    board += "| " + "{:<30}{:>9}{:<1}{:>10}".format(f"Sheldon: {sheldon_choice}",
                                                    "+", int(add_sheldon_pt),
                                                    f"{sheldon_pts}") + " |\n"
    board += "| " + "{:^50}".format(interpret_round(player_choice, sheldon_choice)) + " |\n"
    board += "+{}+".format("-" * scoreboard_width)

    print(board)


def interpret_round(player_choice, sheldon_choice):
    player_choice_str = moves_map.get(player_choice, "")
    sheldon_choice_str = moves_map.get(sheldon_choice,)

    if player_choice == sheldon_choice:
        return f"It's a tie!"
    elif (player_choice, sheldon_choice) in win_lose_combos:
        # finding index of winning combo
        combo_index = win_lose_combos.index((player_choice, sheldon_choice))
        # finding corresponding action
        action = actions[combo_index]
        return f"{player_choice_str.upper()} {action} {sheldon_choice_str.upper()}!"
    else:
        # finding index of losing combo (inverse of winning combo)
        combo_index = win_lose_combos.index((sheldon_choice, player_choice))
        # finding corresponding action
        action = actions[combo_index]
        return f"{sheldon_choice_str.upper()} {action} {player_choice_str.upper()}!"
    

def print_winner(player, player_pts):
    print("\n")
    win_board = "+{}+".format("*~" * win_board_width) + "\n"
    win_board += ">>>" + "{:^48}".format("!!! BAZINGA !!!") + "<<<\n"

    if player_pts == points_to_win:
        win_board += ">>>" + "{:^48}".format(f"{player.title()} outsmarted Sheldon!") + "<<<\n"
    else:
        win_board += ">>>" + "{:^48}".format(f"Sheldon outsmarted {player.title()}!") + "<<<\n"

    win_board += "+{}+".format("*~" * win_board_width) + "\n\n"

    print(win_board)


def print_character_menu():
    character_menu = "Choose your character to begin playing: \n"
    for key, value in character_map.items():
        character_menu += f"({key}) {value}\n"
    print(character_menu)

class InputError(Exception):
    """Raised when input does not match dictionary key or value"""
    pass

def get_character():
    try:
        player_name = check_input(character_map)
        return character_map[player_name]
    except InputError as e:
        print(f"Error: {e}")
