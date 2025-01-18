def true_method():
    return True

def false_method():
    return False

def value1():
    return 10

def value2():
    return 20

def test_if_else_value():
    # if 문이 참이면 앞 값, 거짓이면 뒷 값
    value = value1() if true_method() else value2()
    assert value == 10
    value = value1() if false_method() else value2()
    assert value == 20