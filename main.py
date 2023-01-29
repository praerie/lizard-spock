from src.game import print_character_menu, get_character, print_round_menu, \
    make_move, get_round_winner, create_scoreboard, print_winner
import src.constants as const
import random


print(f"\nBattle Sheldon in {const.title}!\n")

print_character_menu()
player = get_character()

player_pts = 0
sheldon_pts = 0
round_counter = 0
add_player_pt = False
add_sheldon_pt = False

while player_pts < const.points_to_win and sheldon_pts < const.points_to_win:
    round_counter += 1
    print_round_menu(round_counter)

    sheldon_choice = random.choice(const.move)
    player_choice = make_move()

    if player_choice == sheldon_choice:
        add_player_pt = False
        add_sheldon_pt = False
    else:
        add_player_pt = get_round_winner(player_choice, sheldon_choice)
        if int(add_player_pt) == 1:
            player_pts += 1
            add_player_pt = True
            add_sheldon_pt = False
        else:
            sheldon_pts += 1
            add_player_pt = False
            add_sheldon_pt = True

    create_scoreboard(player, player_pts, sheldon_pts, player_choice,
                      sheldon_choice, add_player_pt, add_sheldon_pt)

print_winner(player, player_pts)

print(f"Thank you for playing!")
