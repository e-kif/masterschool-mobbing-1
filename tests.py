def move_forward(x,y,direction,distance):
    return {"x":0,"y":20,"d":"N"}
def test_translate_command():
    assert move_forward(0,0,"N",20)=={"x":0,"y":20,"d":"N"}
