from data.get_battle_result import get_battle_result 

def count_player_losses(battles, player_id):
    losses = 0
    for battle in battles: 
        result = get_battle_result(battle, player_id)
        if result == 'loss':
            losses += 1
    return losses
        