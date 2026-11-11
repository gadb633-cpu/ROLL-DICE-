from game.inputs import get_num,get_name
from game.shaw_result import shaw_round_result,shaw_info,shaw_game_result
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
    scores = {"player_score":0,"computer_score":0}
    name_player = get_name("enter your name")
    rounds = get_num("enter num rounds(1-10)")
    shaw_info(name_player,rounds)
    list_rounds = []
    for round in range(rounds):
        round_result = play_round(name_player,round+1)
        if round_result["winner"] == name_player:
            scores["player_score"] +=1
        elif round_result["winner"] == "Computer":
            scores["computer_score"] +=1 
        list_rounds.append(round_result)
    new_game = save_game(name_player,rounds,list_rounds,scores["player_score"],scores["computer_score"])
    shaw_game_result(new_game)
    return new_game

def calculate_winner(player_score, computer_score,name_player):
    if player_score > computer_score:
        return name_player
    elif player_score < computer_score:
        return "computer"
    else:
        return "draw"
    
def play_round(name_player,round):
    num_player = roll_dice()
    num_Computer = roll_dice()
    winner = check_winner(num_player,num_Computer,name_player)
    new_round = save_round_result(round,num_player,num_Computer,name_player)
    shaw_round_result(new_round,name_player)
    return new_round

def save_game(name_player,rounds,list_rounds,player_score,computer_score):
    game ={
    "player_name": name_player,
    "rounds": rounds,
    "player_score": player_score,
    "computer_score": computer_score,
    "Winner": calculate_winner(player_score,computer_score,name_player),
    "results": list_rounds}
    return game

