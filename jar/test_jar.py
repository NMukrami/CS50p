from jar import Jar
import pytest


def test_init():
    jar = Jar(12)
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# deposit 5 in jar have 5
def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


# deposit 11 and withdraw 6. 11 - 6 = 5
def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(6)
    assert jar.size == 5