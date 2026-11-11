import json

def load_game_history():
    try:
        with open("game_history.json", "r", encoding="utf-8") as file:
            return json.load(file)  
            
    except FileNotFoundError as error:
        print(error)
    except:
        return []

def save_game_to_json(game):
    list_games = load_game_history()
    list_games.append(game)
    with open("game_history.json", "w", encoding="utf-8") as file:
        json.dump(list_games,file,indent=4,ensure_ascii=False)
    return True  