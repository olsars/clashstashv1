from stats.count_player_draws import count_player_draws
from stats.count_player_wins import count_player_wins
from stats.count_player_losses import count_player_losses
from stats.calculate_player_win_rate import calculate_player_win_rate
from stats.calculate_win_streak import calculate_win_streak

def get_player_summary(battles, player_id):
    wins = count_player_wins(battles, player_id)
    losses = count_player_losses(battles, player_id)
    draws = count_player_draws(battles, player_id)
    win_rate = calculate_player_win_rate(battles, player_id)
    win_streaks = calculate_win_streak(battles, player_id)
    longest_win_streak = win_streaks.get("longest_win_streak")
    current_win_streak = win_streaks.get("current_win_streak")

    summary = {
        "player_tag": player_id,
        "total_battles": wins + losses + draws,
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": win_rate,
        "current_win_streak": current_win_streak,
        "longest_win_streak": longest_win_streak
    }
    return summary