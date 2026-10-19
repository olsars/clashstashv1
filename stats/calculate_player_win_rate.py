def calculate_player_win_rate(player_list, player_name):
   player_stats = player_list.get(player_name)
   if player_stats is None:
      return None
   wins = player_stats.get("wins")
   losses = player_stats.get("losses")
   total_matches = wins + losses
   if total_matches == 0:
      return 0
   win_rate = (wins/total_matches) * 100
   return round(win_rate, 2)

