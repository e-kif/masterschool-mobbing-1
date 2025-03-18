from app import move_forward


def test_translate_command():
    assert move_forward(0, 0, "N", 20) == {"x": 0, "y": 20, "d": "N"}
    assert move_forward(0, 0, "N", 10) == {"x": 0, "y": 10, "d": "N"}
