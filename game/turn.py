from tiles import play_set, is_valid_set
from inputs.get_string import get_string




def read_player_move(hand: list):
    valid_move = False
    while not valid_move:
        try:
            user_choice = get_string("Choose tile positions or D to draw > ").strip()
            if user_choice.lower() == "d":
                return None
            numbers_list = user_choice.split(" ")
            if len(numbers_list) < 3:
                raise ValueError("Must be at least 3 numbers")
            numbers = []
            for n in numbers_list:
                if not n.isdigit():
                    raise ValueError(n, "is not a whole number")            
                number = int(n)
                if not (1 <= number <= len(hand)):
                    raise ValueError(f"number {number} is not in valid range")
                number -= 1
                if number in numbers:
                    raise ValueError(f"number {number} is already in lis")
                numbers.append(number)
                
        except ValueError as error:
            print("Error:", error)
        else:
            valid_move = True
    return numbers


def find_computer_move(hand: list):
    valids = []
    numbers = {}
    colors = {}
    for tile in hand:
        if not tile[0] in numbers:
            numbers[tile[0]] = set()
        if not tile[1] in colors:
            numbers[tile[1]] = set()
        numbers[tile[0]].add(tile)
        colors[tile[1]].add(tile)
    for s in numbers:
        if is_valid_set():
            valids.append(s)
    for s in colors:
        by_number = sorted(list(s), key=lambda tile: tile[0])
        for i in range(len(by_number) - 3):
            x = 0
            while i + x + 3 <= len(by_number):
                if is_valid_set(by_number[i: i + 3 + x]):
                    x +=1
                else:
                    break
            if is_valid_set(by_number[i: i + 3 + x - 1]):
                valids.append(by_number[i: i + 3 + x - 1])
    if not valids:
        return None
    longest = sorted(valids, key= lambda p: len(p))[0]
    return longest




def play_turn(hand: list, pool: list, table: list, move):
    if move is None:
        if pool:
            hand.append(pool.pop())
            return "draw"
        return "pass"
    play_set(hand, table, move)
    return "play"