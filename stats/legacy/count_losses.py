def count_losses(matches):
    losses = 0
    for match in matches:
        if match.upper() == "LOSS":
            losses += 1
    return losses
            

