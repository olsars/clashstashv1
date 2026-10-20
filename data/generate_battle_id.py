import hashlib


def generate_battle_id(battle):
    battle_type = battle.get('battle_type')
    battle_time_raw = battle.get('battle_time_raw')
    player_1_tag = battle.get('player_1_tag')
    player_2_tag = battle.get('player_2_tag')
    
    test_dictionary = {
        'battle_type': battle_type,
        'battle_time_raw': battle_time_raw,
        'player_1_tag': player_1_tag,
        'player_2_tag': player_2_tag
    }
    
    for key, value in test_dictionary.items():
        if value is None or value.strip() == "":
            return None
        
    players = [player_1_tag, player_2_tag] 
    players_sorted = sorted(players)

    battle_string = f"{players_sorted[0]}-{players_sorted[1]}-{battle_time_raw}-{battle_type}".encode('utf-8')

    hashed_battle_string = hashlib.sha256(battle_string).hexdigest()
    return hashed_battle_string
    