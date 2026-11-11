import json
import os
def load_game_history():
    try:
        with open("game_history.json", "r", encoding="utf-8") as file:
            return json.load(file)  
            
    except FileNotFoundError as error:
        print(error)
    except:
        return []

# def load_game_history(): 
#     if not os.path.exists("game_history.json"):
#         return []
#     try:
#         with open("game_history.json", "r") as file:
#             return json.load(file)
#     except json.JSONDecodeError:
#         raise IOError("Error decoding JSON from game_history.json\nYOUR JSON NOT WORKING IDIOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def save_game_to_json(game):
    list_games = load_game_history()
    list_games.append(game)
    with open("game_history.json", "w", encoding="utf-8") as file:
        json.dump(list_games,file,indent=4,ensure_ascii=False)
    return True

# def save_game_to_json(game):
#     history = load_game_history()
#     history.append(game)
#     try:
#         with open("game_history.json", "w") as file:
#             json.dump(history, file, indent=4)
#         return True
#     except IOError:
#         return False
  