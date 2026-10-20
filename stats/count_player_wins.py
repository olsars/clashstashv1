from data.get_battle_result import get_battle_result 

def count_player_wins(battles, player_id):
    wins = 0
    for battle in battles: 
        result = get_battle_result(battle, player_id)
        if result == 'win':
            wins += 1
    return wins
        