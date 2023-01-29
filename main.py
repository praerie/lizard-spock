from src.game import get_character, play_round, print_winner
import src.constants as const
import src.mutables as mut

print(f"\nBattle Sheldon in {const.title}!\n")

mut.player = get_character()

while mut.player_points < const.points_to_win and mut.sheldon_points < const.points_to_win:
    mut.round_counter += 1
    play_round()

print_winner()

print(f"Thank you for playing {const.title}!")
