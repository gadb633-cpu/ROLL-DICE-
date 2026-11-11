def shaw_info(name_player,rounds):
    print(f'''
            Player name: {name_player}
            Number of rounds: {rounds}
            ''')
def shaw_round_result(new_round,name_player):
    print(f'''     
        ---------- ROUND {new_round["round"] +1} ----------

            {name_player}:    {new_round["player_dice"]}
            Computer: {new_round["computer_dice"]}

            {new_round["winner"]} wins this round!
        ''')