import string


class InputError(Exception):
    """Raised when input does not fall within range or does not correspond to tuple value"""
    pass


def check_input(data_to_check):
    """Checking input against 'move' and 'character' tuples with associated range"""
    while True:
        try:
            player_input = str(input()).lower().strip()

            # checking if input is digit (length of 1, not character)
            if len(player_input) == 1 and player_input not in string.ascii_lowercase:
                # checking if digit is in tuple range
                if int(player_input) in range(1, len(data_to_check) + 1):
                    return player_input
                raise InputError
            # checking if string is in tuple
            elif player_input in data_to_check:
                return player_input
            raise InputError

        except InputError:
            print("> Oops! Please only enter a word/name above or a number within range.")

