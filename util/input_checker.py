import string


class InputError(Exception):
    """Raised when input does not match dictionary key or value"""
    pass


def check_input(data_to_check):
    """Checking if input matches data_to_check dictionary"""
    while True:
        try:
            player_input = input("> ").lower().strip()

            # checking if valid key 
            if player_input.isdigit() and player_input in data_to_check:
                return player_input
          
            # checking if valid value
            for key, value in data_to_check.items():
                if value.lower() == player_input:
                    return key
            
            raise InputError("Invalid input. Please enter a valid character or number.")
        
        except InputError as e:
            print(f"Error: {e}")

