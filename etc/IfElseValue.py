def test_if_else_value():
    # if 문이 참이면 앞 값, 거짓이면 뒷 값
    value = 10 if True else 20
    assert value == 10
    value = 10 if False else 20
    assert value == 20