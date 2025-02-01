import pytest

def test_pass():
    assert 1 == 1

def test_fail():
    assert 1 == 2

def test_error():
    raise Exception("Error")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0