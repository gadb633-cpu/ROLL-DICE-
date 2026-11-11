def shaw_menu():
    print('''
        ================================
                    ROLL DICE
        ================================

        1. Start New Game
        2. View Game History
        3. View Statistics
        4. Exit
            ''')
    
def shaw_info(name_player,rounds):
    print(f'''  
        ================================
                    NEW GAME
        ================================

        Player name: {name_player}
        Number of rounds: {rounds}
            ''')
def shaw_round_result(new_round,name_player):
    print(f'''     
        ---------- ROUND {new_round["round"]} ----------

            {name_player}:    {new_round["player_dice"]}
            Computer: {new_round["computer_dice"]}

            {new_round["winner"]} wins this round!
        ''')
def shaw_game_result(game):
    print(f'''
        ================================
                    GAME OVER
        ================================

        {game["player_name"]}: {game["player_score"]}
        Computer: {game["computer_score"]}

        WINNER: {game["Winner"]}!

        Game saved successfully!
        ''')    