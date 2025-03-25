def move_forward(x, y, direction, distance):
    data = {
        "x": x,
        "y": y,
        "d": direction
            }
    if direction == "N":
        data["y"] += distance
    elif direction == "S":
        data["y"] -= distance
    elif direction == "E":
        data["x"] += distance
    elif direction == "W":
        data["x"] -= distance
    else:
        print("wrong direction....")
    return data

