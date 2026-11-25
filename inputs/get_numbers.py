from .get_string import validate_input, get_string
from validations.inputs import is_number

def get_integer(message:str)-> int:
    user_input = validate_input(message, is_number, get_string)
    return int(user_input)


