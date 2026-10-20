from data.get_battle_result import get_battle_result

def calculate_win_streak(battles, player_id):
    sorted_battles = sorted(battles, key=lambda battle:battle["battle_time_raw"])
    current_win_streak = 0
    longest_win_streak = 0
    for battle in sorted_battles:
        player_1_tag = battle.get('player_1_tag')
        player_2_tag = battle.get('player_2_tag')
        if player_id != player_1_tag and player_id != player_2_tag:
            continue
        result = get_battle_result(battle, player_id)
        if result == 'win':
            current_win_streak += 1
        else: 
            current_win_streak = 0
        if current_win_streak > longest_win_streak:
            longest_win_streak = current_win_streak
    streaks = {
        "longest_win_streak": longest_win_streak,
        "current_win_streak": current_win_streak
    }
    return streaks