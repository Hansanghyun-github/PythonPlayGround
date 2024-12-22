def test_dynamic_typing():
    a = 5
    b = 5
    assert type(a) is type(b)

def test_dynamic_typing2():
    a = 5
    b = 5.0
    assert type(a) is not type(b)

def test_dynamic_typing3():
    a = 5
    assert type(a) is int