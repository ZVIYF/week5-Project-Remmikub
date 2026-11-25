def print_tiles(title, tile_list: list[tuple]):
    print(f"====== {title} ======\n")
    if not tile_list:
        print(f"EMPTY\n")
    else:
        for i in range(len(tile_list)):
            if i % 5 == 0:
                print()
            print(f"[{i + 1}] {tile_list[i][0]}{tile_list[i][1]}".ljust(8), end=" ")
        print()

def print_turn(table, player, computer):
    print_table(table)
    print(f"Computer Tiles: {len(computer)}")
    print_tiles("Your Hand", player)


def print_table(table):
    print(f"====== TABLE ======\n")
    if not table:
        print(f"EMPTY\n")
    else:
        for i in range(len(table)):
            print()
            print(f"[{i + 1}] ", end=" ")
            for tile in table[i]:
                print(f"[{tile[0]}{tile[1]}]".ljust(4), end=" ")
                
        print()