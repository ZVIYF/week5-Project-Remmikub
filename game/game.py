from .tiles import create_pool, take_tile
from prints.game_prints import print_tiles, print_turn
from .turn import read_player_move


def play_game():

    pool = create_pool()
    table = []
    player_hand = []
    computer_hand = []
    pass_counter = 0
    for _ in range(9):
        take_tile(pool, player_hand)
        take_tile(pool, computer_hand)
    running = True
    while running:
        print_turn(table, player_hand, computer_hand)
        p_move = read_player_move()
        if not player_hand:
            print("Player wins!")
            running = False
            continue
        if (p_move == "play") or (p_move == "draw"):
            pass_counter = 0
        else:
            pass_counter += 1
        


def check_winner(pass_counter, player_hand, commputer_hand):
    