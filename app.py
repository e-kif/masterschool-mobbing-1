class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move_forward(self, distance=1):
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
        return {
            "x": self.x,
            "y": self.y,
            "d": self.direction
        }

    def turn_right(self):
        mapping = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        self.direction = mapping[self.direction]
        return {"x": self.x, "y": self.y, "d": self.direction}

    def turn_left(self):
        mapping = {
            "N": "W",
            "E": "N",
            "S": "E",
            "W": "S"
        }
        self.direction = mapping[self.direction]
        return {"x": self.x, "y": self.y, "d": self.direction}

    def move_backwards(self):
        pass

    def receive_command(self, commands: list[str]):
        command_mapping = {'F': self.move_forward, 'L': self.turn_left, 'R': self.turn_right, 'B': self.move_backwards}
        for command in commands:
            if command in command_mapping.keys():
                command_mapping[command]

