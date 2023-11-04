from plates import is_valid

def test_is_valid():
    assert is_valid("S5") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False