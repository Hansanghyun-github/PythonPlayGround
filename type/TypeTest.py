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

def test_integer_range():
    n = 300
    assert type(n) is int
    n = 2**65
    assert type(n) is int

def test_float_range():
    n = 300.0
    assert type(n) is float
    n = 1.7e308 + 1
    assert type(n) is float

def test_type_with_hunting():
    n: int = 300
    assert type(n) is int
    n = "300"
    assert type(n) is str
    # type hunting doesn't pre-occur error