class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move_forward(self, distance):
        data = {
            "x": self.x,
            "y": self.y,
            "d": self.direction
        }
        if self.direction == "N":
            self.y += distance
        elif self.direction == "S":
            self.y -= distance
        elif self.direction == "E":
            self.x += distance
        elif self.direction == "W":
            self.x -= distance
        else:
            print("wrong direction....")
        return data

    def turn_right(self, direction):
        mapping = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        self.direction = mapping[direction]
        return {"x": x, "y": y, "d": mapping[direction]}

    def turn_left(x, y, direction):
        mapping = {
            "N": "W",
            "E": "N",
            "S": "E",
            "W": "S"
        }
        return {"x": x, "y": y, "d": mapping[direction]}

    def move_backwards(self):
        pass
