def longest_win_streak(matches):
    win_streak = 0
    highest_streak = 0
    if len(matches) == 0:
        return 0
    for match in matches:
        if match.upper() == "WIN":
            win_streak += 1
        else: 
            win_streak = 0
        if win_streak > highest_streak:
            highest_streak = win_streak
    return highest_streak
