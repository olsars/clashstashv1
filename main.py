from stats.get_player_summary import get_player_summary
from data.players import players
from data.load_battles import load_battles
from data.process_battles import process_battles
from data.get_battle_result import get_battle_result
import json 

"""
for key, value in players.items():
    label = key.title().replace("_"," ")
    print(f"{label}: ")
        
    for key_2 in value:
          label = key_2.title().replace("_", " ")
          print(f"{label}: {value[key_2]}")
    print(f"Win Rate: {calculate_player_win_rate(processed, "#9V02LJ8VL")}%")
    print("\n")
    """

battles = load_battles("data/sample_battles.json")
processed = process_battles(battles)

print(type(processed))
print(len(processed))

i = 0
while i < len(processed):
    print(processed[i])
    i+=1
print(get_battle_result(processed[0], "#9V02LJ8VL"))
print(get_player_summary(processed, "#9V02LJ8VL"))