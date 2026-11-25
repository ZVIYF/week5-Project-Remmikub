from .tiles import create_pool, take_tile
from prints.game_prints import print_turn
from .turn import read_player_move, find_computer_move, play_turn


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
        p_move = read_player_move(player_hand)
        move = play_turn(player_hand, pool, table, p_move)
        if (move == "play") or (move == "draw"):
            pass_counter = 0
        else:
            pass_counter += 1
        winner = check_winner(pass_counter, player_hand, computer_hand)
        if winner is not None:
            print(f"Winner: {winner}!")
            running = False
            continue
        c_move = find_computer_move(computer_hand)
        move = play_turn(computer_hand, pool, table, c_move)
        if (move == "play") or (move == "draw"):
            pass_counter = 0
        else:
            pass_counter += 1
        winner = check_winner(pass_counter, player_hand, computer_hand)
        if winner is not None:
            print(f"Winner: {winner}!")
            running = False
            continue



def check_winner(pass_counter, player_hand, computer_hand):
    if pass_counter == 2:
        if len(player_hand) > len(computer_hand):
            return "computer"
        if len(player_hand) < len(computer_hand):
            return "player"
        return "draw"
    if not player_hand:
        return "player"
    if not computer_hand:
        return "computer"
    return None