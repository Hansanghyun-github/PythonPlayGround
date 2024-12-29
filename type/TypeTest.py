def test_dynamic_typing():
    n = 300
    assert type(n) is int
    n = "300"
    assert type(n) is str

def test_dynamic_typing2():
    n = 300
    assert type(n) is int
    n = 300.0
    assert type(n) is float