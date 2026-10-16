from get_match_summary import get_match_summary
match_history = [
    "loss", "win", "win", "win",
    "win", "loss", "win", "loss"
]

stats = get_match_summary(match_history)
print("---- MATCH SUMMARY ----")
for key, value in stats.items():
    label = key.replace("_"," ").title()
    if key == "win_rate":
         print(f"{label}: {value}%")
    else:
          print(f"{label}: {value}")
