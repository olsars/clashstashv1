from count_matches import count_matches
from count_losses import count_losses
from count_wins import count_wins
from calculate_win_rate import calculate_win_rate
from longest_win_streak import longest_win_streak

def get_match_summary(matches):
    summary = {
        "total_matches": count_matches(matches),
        "losses": count_losses(matches),
        "wins": count_wins(matches),
        "win_rate": round(calculate_win_rate(matches), 2),
        "longest_streak": longest_win_streak(matches)
    }
    return summary

"""
print("CLASH - STASH")
print(f"Total Matches Played: {total_matches}")
print(f"Total Wins: {wins}")
print(f"Total Losses: {losses}")
print(f"Win Rate: {round(win_rate, 1)}%")
print(f"Highest Win Streak: {longest_streak}")
"""