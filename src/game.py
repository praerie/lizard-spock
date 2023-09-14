from util.input_checker import check_input
import src.const as const


def print_round_menu(round_counter):
    round_menu = f"\nRound #{round_counter}:\n"
    round_menu += "{:<12}{:<12}{:<12}".format(f"(1) {const.rock}", f"(2) {const.paper}", f"(3) {const.scissors}") + "\n"
    round_menu += "{:^36}".format(f"(4) {const.lizard} \t (5) {const.spock}")
    print(round_menu)


def make_move():
    player_move = check_input(const.move)

    if player_move == "1" or player_move == const.rock:
        return const.move[0]
    elif player_move == "2" or player_move == const.paper:
        return const.move[1]
    elif player_move == "3" or player_move == const.scissors:
        return const.move[2]
    elif player_move == "4" or player_move == const.lizard:
        return const.move[3]
    elif player_move == "5" or player_move == const.spock:
        return const.move[4]


def get_round_winner(player_choice, sheldon_choice):
    if (player_choice, sheldon_choice) in const.win_lose_combos:
        return True
    else:
        return False


def create_scoreboard(player, player_pts, sheldon_pts, player_choice,
                      sheldon_choice, add_player_pt, add_sheldon_pt):
    board = "+{}+".format("-" * const.scoreboard_width) + "\n"
    board += "| " + "{:<30}{:>9}{:<1}{:>10}".format(f"{player.title()}: {player_choice}",
                                                    "+", int(add_player_pt),
                                                    f"{player_pts}") + " |\n"
    board += "| " + "{:<30}{:>9}{:<1}{:>10}".format(f"Sheldon: {sheldon_choice}",
                                                    "+", int(add_sheldon_pt),
                                                    f"{sheldon_pts}") + " |\n"
    board += "| " + "{:^50}".format(interpret_round(player_choice, sheldon_choice)) + " |\n"
    board += "+{}+".format("-" * const.scoreboard_width)

    print(board)


def interpret_round(player_choice, sheldon_choice):
    if player_choice == sheldon_choice:
        return f"It's a tie!"
    elif (player_choice, sheldon_choice) in const.win_lose_combos:
        # finding pos of winning combo in win_lose_combos tuple
        # to correspond to pos in actions tuple
        combo = (player_choice, sheldon_choice)
        combo_pos = const.win_lose_combos.index(combo)

        return f"{player_choice.upper()} {const.actions[combo_pos]} {sheldon_choice.upper()}!"
    else:
        # finding pos of lose-win combo in win_lose_combos tuple (inverse of win-lose pairs)
        # to correspond to pos in actions tuple
        combo = (sheldon_choice, player_choice)
        combo_pos = const.win_lose_combos.index(combo)

        return f"{sheldon_choice.upper()} {const.actions[combo_pos]} {player_choice.upper()}!"
    

def print_winner(player, player_pts):
    print("\n")
    win_board = "+{}+".format("*~" * const.win_board_width) + "\n"
    win_board += ">>>" + "{:^48}".format("!!! BAZINGA !!!") + "<<<\n"

    if player_pts == const.points_to_win:
        win_board += ">>>" + "{:^48}".format(f"{player.title()} outsmarted Sheldon!") + "<<<\n"
    else:
        win_board += ">>>" + "{:^48}".format(f"Sheldon outsmarted {player.title()}!") + "<<<\n"

    win_board += "+{}+".format("*~" * const.win_board_width) + "\n\n"

    print(win_board)


def print_character_menu():
    character_menu = "Choose your character to begin playing: \n"
    character_menu += "{:<14}{:<14}".format(f"(1) {const.leonard}", f"(2) {const.amy}") + "\n"
    character_menu += "{:<14}{:<14}".format(f"(3) {const.raj}", f"(4) {const.bernadette}") + "\n"
    character_menu += "{:<14}{:<14}".format(f"(5) {const.penny}", f"(6) {const.stuart}") + "\n"
    character_menu += "{:<14}{:<14}".format(f"(7) {const.howard}", f"(8) {const.leslie}") + "\n"
    character_menu += f"(9) {const.professor_proton}"
    print(character_menu)


def get_character():
    player_name = check_input(const.character)

    if player_name == "1" or player_name == const.leonard:
        return const.character[0]
    elif player_name == "2" or player_name == const.amy:
        return const.character[1]
    elif player_name == "3" or player_name == const.raj:
        return const.character[2]
    elif player_name == "4" or player_name == const.bernadette:
        return const.character[3]
    elif player_name == "5" or player_name == const.penny:
        return const.character[4]
    elif player_name == "6" or player_name == const.stuart:
        return const.character[5]
    elif player_name == "7" or player_name == const.howard:
        return const.character[6]
    elif player_name == "8" or player_name == const.leslie:
        return const.character[7]
    elif player_name == "9" or player_name == const.professor_proton:
        return const.character[8]
