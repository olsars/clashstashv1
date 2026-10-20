from data.get_battle_result import get_battle_result 

def count_player_draws(battles, player_id):
    draws = 0
    for battle in battles: 
        result = get_battle_result(battle, player_id)
        if result == 'draw':
            draws += 1
    return draws
        