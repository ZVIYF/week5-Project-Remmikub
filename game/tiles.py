from random import shuffle

def create_deck()-> list:
    deck = []
    colors = ["R", "B", "K", "O"]
    for color in colors:
        for number in range(1, 14):
            deck.append((number, color))
            deck.append((number, color))
    return deck


def shuffle_deck(deck:list)-> None:
    shuffle(deck)


def create_pool()-> list:
    deck = create_deck()
    shuffle_deck(deck)
    return deck


def is_valid_set(tiles: set|list)-> bool:
    if len(tiles) < 3:
        return False
    colors = set()
    for tile in tiles:
        colors.add(tile[1])
    sequance = sorted(tiles, key=lambda t: t[0]) 
    if len(colors) == 1:
        return check_numbers_sequance(sequance)
    if len(colors) == len(tiles):
        return check_numbers_sequance(sequance, difference=0)
    return False


def check_numbers_sequance(tiles: list, difference = 1)-> bool:
    if len(tiles) == 1:
        return True
    if (tiles[0][0] + difference) != tiles[1][0]:
        return False
    return check_numbers_sequance(tiles[1:], difference)


def play_set(hand: list, table: list, indexes: list):
    sort_indexes = sorted(indexes, reverse=True)
    move = []
    for index in sort_indexes:
        tile = hand.pop(index)
        move.append(tile)
    table.append(move)


def take_tile(pool: list, hand:list):
    hand.append(pool.pop())