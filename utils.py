import json
from datetime import datetime

def save_game_history(winner, loser, result):
    history_file = 'history.json'
    history_data = {
        "winner": winner,
        "loser": loser,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(history_file, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(history_data)

    with open(history_file, 'w') as f:
        json.dump(data, f, indent=4)
