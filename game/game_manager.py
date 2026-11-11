
def check_winner(num_player,num_Computer,name_player):
    if num_player > num_Computer:
        return name_player
    elif num_player < num_Computer:
        return "Computer"
    else:
        return "draw"

def save_round_result(num_round,num_player,num_Computer,name_player):
    new_round = {
            "round": num_round,
            "player_dice": num_player,
            "computer_dice": num_Computer,
            "winner": check_winner(num_player,num_Computer,name_player)}
    return new_round


