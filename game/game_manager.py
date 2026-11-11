from game.inputs import get_num,get_name
from game.shaw_result import shaw_round_result,shaw_info
from game.roll_dice_random import roll_dice

def check_winner(num_player,num_Computer,name_player):
    if num_player > num_Computer:
        return name_player
    elif num_player < num_Computer:
        return "Computer"
    else:
        return "draw"

def save_round_result(round,num_player,num_Computer,name_player):
    new_round = {
            "round": round,
            "player_dice": num_player,
            "computer_dice": num_Computer,
            "winner": check_winner(num_player,num_Computer,name_player)}
    return new_round
def start_game():
    name_player = get_name("enter your name")
    rounds = get_num("enter num rounds(1-10)")
    shaw_info(name_player,rounds)
    for round in range(rounds):
        round_result = play_round(name_player,round)

def play_round(name_player,round):
    num_player = roll_dice()
    num_Computer = roll_dice()
    winner = check_winner(num_player,num_Computer,name_player)
    new_round = save_round_result(round,num_player,num_Computer,name_player)
    shaw_round_result(new_round,name_player)

def save_game():
    pass
