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
def shaw_Game_History(games):
    if games ==[]:
        shaw_msg()
    else:    
        for game in games:
            print(f'''
                player name: {game["player_name"]}
                rounds: {game["rounds"]}
                player_score: {game["player_score"]}
                computer_score: {game["computer_score"]}
                Winner: {game["Winner"]}
        ''')
def shaw_View_Statistics(games):
    if games ==[]:
        shaw_msg()   
    else:
        total_games = len(games)
        computer_wins = sum(1 for game in games if game["Winner"] == "Computer")
        draw = sum(1 for game in games if game["Winner"] == "draw")
        player_wins = total_games - draw -computer_wins
        print(f"Total Games: {total_games}")
        print(f"Player Wins: {player_wins} ({(player_wins / total_games) * 100:.2f}%)")
        print(f"Computer Wins: {computer_wins} ({(computer_wins / total_games) * 100:.2f}%)")
        print(f"draw: {draw} ({(draw / total_games) * 100:.2f}%)\n")  

def shaw_msg():
    print("no games")        