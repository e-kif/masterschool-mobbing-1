from app import move_forward, turn_right, turn_left


def test_move_forward():
    assert move_forward(0, 0, "N", 20) == {"x": 0, "y": 20, "d": "N"}
    assert move_forward(0, 0, "N", 10) == {"x": 0, "y": 10, "d": "N"}
    assert move_forward(0, 10, "N", 10) == {"x": 0, "y": 20, "d": "N"}

    assert move_forward(0, 0, "S", 20) == {"x": 0, "y": -20, "d": "S"}
    assert move_forward(0, 0, "S", 10) == {"x": 0, "y": -10, "d": "S"}
    assert move_forward(0, 10, "S", 10) == {"x": 0, "y": 0, "d": "S"}

    assert move_forward(0, 0, "W", 20) == {"x": -20, "y": 0, "d": "W"}
    assert move_forward(0, 0, "W", 10) == {"x": -10, "y": 0, "d": "W"}
    assert move_forward(0, 10, "W", 10) == {"x": -10, "y": 10, "d": "W"}

    assert move_forward(0, 0, "E", 20) == {"x": 20, "y": 0, "d": "E"}
    assert move_forward(0, 0, "E", 10) == {"x": 10, "y": 0, "d": "E"}
    assert move_forward(0, 10, "E", 10) == {"x": 10, "y": 10, "d": "E"}


def test_turn_command():
    assert turn_right(0, 0, "N") == {"x": 0, "y": 0, "d": "E"}
    assert turn_right(0, 0, "E") == {"x": 0, "y": 0, "d": "S"}
    assert turn_right(0, 10, "S") == {"x": 0, "y": 10, "d": "W"}
    assert turn_right(0, 10, "W") == {"x": 0, "y": 10, "d": "N"}

    assert turn_left(0, 0, "N") == {"x": 0, "y": 0, "d": "W"}
    assert turn_left(0, 0, "E") == {"x": 0, "y": 0, "d": "N"}
    assert turn_left(0, 10, "S") == {"x": 0, "y": 10, "d": "E"}
    assert turn_left(0, 10, "W") == {"x": 0, "y": 10, "d": "S"}


def test_move_backward():
    assert move_backwards(0, 0, "N", 20) == {"x": 0, "y": -20, "d": "N"}
    assert move_backwards(0, 0, "N", 10) == {"x": 0, "y": -10, "d": "N"}
    assert move_backwards(0, 10, "N", 10) == {"x": 0, "y": 0, "d": "N"}

    assert move_backwards(0, 0, "S", 20) == {"x": 0, "y": 20, "d": "S"}
    assert move_backwards(0, 0, "S", 10) == {"x": 0, "y": 10, "d": "S"}
    assert move_backwards(0, 10, "S", 10) == {"x": 0, "y": 0, "d": "S"}

    assert move_backwards(0, 0, "W", 20) == {"x": -20, "y": 20, "d": "W"}
    assert move_backwards(0, 0, "W", 10) == {"x": -10, "y": 0, "d": "W"}
    assert move_backwards(0, 10, "W", 10) == {"x": -10, "y": 10, "d": "W"}

    assert move_backwards(0, 0, "E", 20) == {"x": 20, "y": 0, "d": "E"}
    assert move_backwards(0, 0, "E", 10) == {"x": 10, "y": 0, "d": "E"}
    assert move_backwards(0, 10, "E", 10) == {"x": 10, "y": 10, "d": "E"}
