import pytest
from hello import greet

def test_greet_world_default():
    assert greet("") == "Hello, World!"

def test_greet_specific_name():
    assert greet("Alice") == "Hello, Alice!"

@pytest.mark.parametrize("name,expected", [
    ("Bob", "Hello, Bob!"),
    ("Éva", "Hello, Éva!"),
    (" ", "Hello, !")
])
def test_greet_various(name, expected):
    assert greet(name) == expected
