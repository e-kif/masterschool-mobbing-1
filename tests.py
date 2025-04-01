from app import Rover


# def test_move_forward():
#     rover = Rover(0, 0, 20)
#     assert rover.move_forward(0, 0, "N", 20) == {"x": 0, "y": 20, "d": "N"}
#     assert rover.move_forward(0, 0, "N", 10) == {"x": 0, "y": 10, "d": "N"}
#     assert rover.move_forward(0, 10, "N", 10) == {"x": 0, "y": 20, "d": "N"}
#
#     assert rover.move_forward(0, 0, "S", 20) == {"x": 0, "y": -20, "d": "S"}
#     assert rover.move_forward(0, 0, "S", 10) == {"x": 0, "y": -10, "d": "S"}
#     assert rover.move_forward(0, 10, "S", 10) == {"x": 0, "y": 0, "d": "S"}
#
#     assert rover.move_forward(0, 0, "W", 20) == {"x": -20, "y": 0, "d": "W"}
#     assert rover.move_forward(0, 0, "W", 10) == {"x": -10, "y": 0, "d": "W"}
#     assert rover.move_forward(0, 10, "W", 10) == {"x": -10, "y": 10, "d": "W"}
#
#     assert rover.move_forward(0, 0, "E", 20) == {"x": 20, "y": 0, "d": "E"}
#     assert rover.move_forward(0, 0, "E", 10) == {"x": 10, "y": 0, "d": "E"}
#     assert rover.move_forward(0, 10, "E", 10) == {"x": 10, "y": 10, "d": "E"}


# def test_turn_command():
#     rover = Rover(0,0, "N")
#     assert rover.turn_right(0, 0, "N") == {"x": 0, "y": 0, "d": "E"}
#     assert rover.turn_right(0, 0, "E") == {"x": 0, "y": 0, "d": "S"}
#     assert rover.turn_right(0, 10, "S") == {"x": 0, "y": 10, "d": "W"}
#     assert rover.turn_right(0, 10, "W") == {"x": 0, "y": 10, "d": "N"}
#
#     assert rover.turn_left(0, 0, "N") == {"x": 0, "y": 0, "d": "W"}
#     assert rover.turn_left(0, 0, "E") == {"x": 0, "y": 0, "d": "N"}
#     assert rover.turn_left(0, 10, "S") == {"x": 0, "y": 10, "d": "E"}
#     assert rover.turn_left(0, 10, "W") == {"x": 0, "y": 10, "d": "S"}


# def test_move_backward():
#    assert move_backwards(0, 0, "N", 20) == {"x": 0, "y": -20, "d": "N"}
#    assert move_backwards(0, 0, "N", 10) == {"x": 0, "y": -10, "d": "N"}
#    assert move_backwards(0, 10, "N", 10) == {"x": 0, "y": 0, "d": "N"}
#
#    assert move_backwards(0, 0, "S", 20) == {"x": 0, "y": 20, "d": "S"}
#    assert move_backwards(0, 0, "S", 10) == {"x": 0, "y": 10, "d": "S"}
#    assert move_backwards(0, 10, "S", 10) == {"x": 0, "y": 0, "d": "S"}
#
#    assert move_backwards(0, 0, "W", 20) == {"x": -20, "y": 20, "d": "W"}
#    assert move_backwards(0, 0, "W", 10) == {"x": -10, "y": 0, "d": "W"}
#    assert move_backwards(0, 10, "W", 10) == {"x": -10, "y": 10, "d": "W"}
#
#    assert move_backwards(0, 0, "E", 20) == {"x": 20, "y": 0, "d": "E"}
#    assert move_backwards(0, 0, "E", 10) == {"x": 10, "y": 0, "d": "E"}
#    assert move_backwards(0, 10, "E", 10) == {"x": 10, "y": 10, "d": "E"}


def test_rover_commands():
    # assert command_array == [move_forward, turn_right, turn_left, move_backward]
    rover = Rover(0, 0, "N")
    assert isinstance(rover, Rover)
    assert rover.__getattribute__("move_forward")
    assert rover.__getattribute__("move_backwards")
    assert rover.__getattribute__("turn_left")
    assert rover.__getattribute__("turn_right")


def test_receive_commands():
    rover = Rover(0, 0, "N")
    assert rover.move_forward(20) == {"x": 0, "y": 20, "d": "N"}
    assert rover.turn_left() == {"x": 0, "y": 20, "d": "W"}
    assert rover.turn_right() == {"x": 0, "y": 20, "d": "N"}


def test_command_array():
    rover = Rover(0, 0, "N")
    assert rover.receive_command(['F', 'L', 'F', 'R', 'B'])
    assert rover.coordinates == (-1, 0, "N")


def test_get_coordinates():
    pass
