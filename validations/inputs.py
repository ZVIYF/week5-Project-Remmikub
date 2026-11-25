def is_string(user_input:str):
    if not user_input:
        raise ValueError("Please type anything")


def is_number(user_input:str):
    if not user_input.isdigit():
        raise ValueError("Input must be a number")
    