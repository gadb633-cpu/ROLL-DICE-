from game.game_manager import start_game
from game.shaw_result import shaw_menu,shaw_Game_History,shaw_View_Statistics
from game.inputs import get_num
from game.save_and_load_json import load_game_history
def main():
    while True:
        shaw_menu()
        choice = get_num("enter your choice(1-4)")
        if choice not in [1,2,3,4]:
            continue
        if choice ==1:
            start_game()
        elif choice ==2:
            shaw_Game_History(load_game_history())
        elif choice ==3:
            shaw_View_Statistics(load_game_history())
        elif choice ==4:
            break

if __name__ == "__main__":
    main()    