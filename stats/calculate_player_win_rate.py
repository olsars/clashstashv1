from stats.count_player_draws import count_player_draws
from stats.count_player_wins import count_player_wins
from stats.count_player_losses import count_player_losses


def calculate_player_win_rate(battle, player_id):
   wins = count_player_wins(battle, player_id)
   losses = count_player_losses(battle, player_id)
   draws  = count_player_draws(battle, player_id)
   total_matches = draws + losses + wins 
   if total_matches == 0:
      return 0
   win_rate = (wins/total_matches) * 100
   return round(win_rate, 2)