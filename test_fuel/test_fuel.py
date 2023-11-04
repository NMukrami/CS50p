from fuel import convert, gauge
import pytest


def test_convert_gauge():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("99/100") == 99 and gauge(99) == "F"