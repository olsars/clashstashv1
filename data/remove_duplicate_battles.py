from generate_battle_id import generate_battle_id

def remove_duplicate_battles(battles):
    unique_ids = set()
    unique_battles = []
    
    for battle in battles:
        current_battle_id = generate_battle_id(battle)
        if current_battle_id is None:
            continue
        if current_battle_id not in unique_ids:
            unique_ids.add(current_battle_id)
            unique_battles.append(battle)

    if not unique_ids:
        return []
    if not unique_battles:
        return []
    
    return unique_battles
        
