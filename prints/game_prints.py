def print_tiles(title, tile_list: list[tuple]):
    print(f"====== {title} ======\n")
    if not tile_list:
        print(f"EMPTY\n")
    else:
        for i in range(len(tile_list)):
            print(f"[{i + 1}] {tile_list[i][0]}{tile_list[i][1]}".ljust(8), end=" ")
            if i % 5 == 0:
                print()

def print_turn(table, player, computer):
    print_tiles("Table", table)
    print(f"Computer Tiles: {len(computer)}")
    print_tiles("Your Hand", player)
    