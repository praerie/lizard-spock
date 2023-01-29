import src.constants as const
import src.mutables as mut


def create_scoreboard():
    board = "+{}+".format("-" * const.scoreboard_width) + "\n"
    board += "| " + "{:<30}{:>9}{:<1}{:>10}".format(f"{mut.player.title()}: {mut.player_choice}",
                                                    "+", int(mut.add_player_point),
                                                    f"{mut.player_points}") + " |\n"
    board += "| " + "{:<30}{:>9}{:<1}{:>10}".format(f"Sheldon: {mut.sheldon_choice}",
                                                    "+", int(mut.add_sheldon_point),
                                                    f"{mut.sheldon_points}") + " |\n"
    board += "| " + "{:^50}".format(interpret_round()) + " |\n"
    board += "+{}+".format("-" * const.scoreboard_width)

    print(board)


def get_score():
    if mut.player_choice == mut.sheldon_choice:
        mut.add_player_point = False
        mut.add_sheldon_point = False
        create_scoreboard()
    elif (mut.player_choice, mut.sheldon_choice) in const.win_lose_combos:
        mut.player_points += 1
        mut.add_player_point = True
        mut.add_sheldon_point = False
        create_scoreboard()
    else:
        mut.sheldon_points += 1
        mut.add_player_point = False
        mut.add_sheldon_point = True
        create_scoreboard()


def interpret_round():
    if mut.player_choice == mut.sheldon_choice:
        return f"It's a tie!"
    elif (mut.player_choice, mut.sheldon_choice) in const.win_lose_combos:
        # finding pos of winning combo in win_lose_combos tuple
        # to correspond to pos in actions tuple
        combo = (mut.player_choice, mut.sheldon_choice)
        combo_pos = const.win_lose_combos.index(combo)

        return f"{mut.player_choice.title()} {const.actions[combo_pos]} {mut.sheldon_choice}!"
    else:
        # finding pos of losing combo in win_lose_combos tuple (inverse of winning)
        # to correspond to pos in actions tuple
        combo = (mut.sheldon_choice, mut.player_choice)
        combo_pos = const.win_lose_combos.index(combo)

        return f"{mut.sheldon_choice.title()} {const.actions[combo_pos]} {mut.player_choice}!"
