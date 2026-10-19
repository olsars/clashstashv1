def count_wins(matches):
    wins = 0
    for match in matches:
        if match.upper() == "WIN":
            wins += 1
    return wins
            

