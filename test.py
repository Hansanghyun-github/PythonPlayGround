import pytest

def test_pass():
    assert 1 == 1

def test_fail():
    assert 1 == 2

def test_error():
    raise Exception("Error")