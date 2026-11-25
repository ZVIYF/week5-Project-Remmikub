from validations.inputs import is_string
from .validator import validate_input

def get_string(message:str)-> str:
    return validate_input(message, is_string)
