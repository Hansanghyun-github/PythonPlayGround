def test_equality():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    assert a == b
    assert a == c

def test_identity():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    assert a is b
    assert a is not c
