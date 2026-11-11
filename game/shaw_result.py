
def shaw_round_result(round,name_player):
    print(f'''
        ---------- ROUND {round["round"]} ----------

            {name_player}:    {round["player_dice"]}
            Computer: {round["computer_dice"]}

            {round["winner"]} wins this round!
        ''')