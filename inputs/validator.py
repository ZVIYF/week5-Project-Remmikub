def validate_input(message:str, validation:function, previus_input = None):
    valid = False
    while not valid:
        # בחירת קלט
        if previus_input is None:
            user_input = input(message).strip()
        else:
            user_input = previus_input(message)    
        # אימות
        try:
            validation(user_input)
        except ValueError as error:
            print("Error:", error)
        else:
            valid = True
    return user_input