def format_battle_time(timestamp):
    year = timestamp[0:4]
    month = timestamp[4:6]
    day = timestamp[6:8]
    hour = timestamp[9:11]
    minute = timestamp[11:13]
    second = timestamp[13:15]
    if 24 > int(hour) > 12:
        hour = int(hour) - 12 
        formatted_time = f"{year}-{month}-{day} {hour}:{minute}:{second} PM"
    elif int(hour) == 12:
        formatted_time = f"{year}-{month}-{day} {hour}:{minute}:{second} PM"
    elif int(hour) == 0:
        hour = 12
        formatted_time = f"{year}-{month}-{day} {hour}:{minute}:{second} AM"
    else: 
        formatted_time = f"{year}-{month}-{day} {hour}:{minute}:{second} AM"
    return formatted_time