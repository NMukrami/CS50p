from bank import value

def test_value():
    # without case-insensitivity
    assert value("Hello") == 0
    # not allowing for entire phrase
    assert value("Hey") == 20