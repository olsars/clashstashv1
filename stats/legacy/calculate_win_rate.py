from stats.legacy.count_wins import count_wins
from stats.legacy.count_matches import count_matches

def calculate_win_rate(matches):
    if len(matches) == 0:
        return 0
    total_matches = count_matches(matches)
    total_wins = count_wins(matches)
    win_rate = (total_wins / total_matches) * 100
    return win_rate