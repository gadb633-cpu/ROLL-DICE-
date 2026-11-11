from game.game_manager import start_game
from game.shaw_result import shaw_menu
from game.inputs import get_num
def main():
    while True:
        shaw_menu()
        choice = get_num("enter your choice(1-4)")
        if choice not in [1,2,3,4]:
            continue
        if choice ==1:
            start_game()
        elif choice ==2:
            pass
        elif choice ==3:
            pass
        elif choice ==4:
            break

if __name__ == "__main__":
    main()    