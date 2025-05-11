import pytest

def test_pass():
    assert 1 == 1

def test_error():
    with pytest.raises(Exception):
        raise Exception("Error")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
