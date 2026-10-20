# Check if specific player won a specific battle
def get_battle_result(battle, player_id):
    player_1_tag = battle.get('player_1_tag')
    player_2_tag = battle.get('player_2_tag')
    player_1_crowns = battle.get('player_1_crowns')
    player_2_crowns = battle.get('player_2_crowns')
    if player_id == player_1_tag:
        player_crowns = battle.get('player_1_crowns')
        opponent_crowns = battle.get('player_2_crowns')

    elif player_id == player_2_tag:
        player_crowns = battle.get('player_2_crowns')
        opponent_crowns = battle.get('player_1_crowns')

    else:
        return None

    if player_crowns > opponent_crowns:
        return 'win'
    elif player_crowns < opponent_crowns:
        return 'loss'
    else:
        return 'draw'
