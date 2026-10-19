from data.format_battle_time import format_battle_time

def extract_battle_info(battles, battle):
   battleTime = format_battle_time(battles[battle]["battleTime"])
   match = {
      "battle_time": battleTime,
      "battle_type": battles[battle]["type"],
      "player_1": battles[battle]['team'][0]['name'],
      "player_1_tag": battles[battle]['team'][0]['tag'],
      "player_1_crowns": battles[battle]['team'][0]['crowns'],
      "player_2": battles[battle]['opponent'][0]['name'],
      "player_2_tag": battles[battle]['opponent'][0]['tag'],
      "player_2_crowns": battles[battle]['opponent'][0]['crowns']
   }
   return match
    


