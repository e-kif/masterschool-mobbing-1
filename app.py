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


def turn_right(x, y, direction):
    mapping = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }
    return {"x": x, "y": y, "d": mapping[direction]}


def turn_left(x, y, direction):
    mapping = {
        "N": "W",
        "E": "N",
        "S": "E",
        "W": "S"
    }
    return {"x": x, "y": y, "d": mapping[direction]}
