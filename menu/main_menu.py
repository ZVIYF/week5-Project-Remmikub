from prints.menu_prints import print_main_menu, print_invalid_choice
from inputs.menu_choice import get_menu_choice
from game.game import play_game


def run():
    main_menu()


def main_menu():
    running = True
    while running:
        print_main_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                play_game()
            case 2:
                running = False
            case _:
                print_invalid_choice()
