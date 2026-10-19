from stats.legacy.get_match_summary import get_match_summary
from stats.calculate_player_win_rate import calculate_player_win_rate
from data.players import players
from data.load_battles import load_battles
from data.process_battles import process_battles
import json 

for key, value in players.items():
    label = key.title().replace("_"," ")
    print(f"{label}: ")
        
    for key_2 in value:
          label = key_2.title().replace("_", " ")
          print(f"{label}: {value[key_2]}")
    print(f"Win Rate: {calculate_player_win_rate(players, key)}%")
    print("\n")


battles = load_battles("data/sample_battles.json")
processed = process_battles(battles)
print(type(processed))
print(len(processed))
print(processed[0]["player_1"])