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

def test_if_else_value_with_for_loop():
    list = [1, 2, 3, 4, 5]
    list2 = [i for i in list if i%2 == 0]
    assert list2 == [2, 4]

def test_in():
    list = [1, 2, 3, 4, 5]
    assert 1 in list
    assert 6 not in list
