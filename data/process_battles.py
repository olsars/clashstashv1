from data.load_battles import load_battles
from data.extract_battle_info import extract_battle_info

def process_battles(battles):
    i = 0
    processed_battles = []
    while i < len(battles):
        extracted = extract_battle_info(battles, i)
        processed_battles.append(extracted)
        i += 1
        print("\n")
    return processed_battles


