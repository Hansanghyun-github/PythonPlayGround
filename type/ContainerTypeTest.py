def test_list():
    list1 = [1, 2, 3, 4, 5]
    assert type(list1) == list

def test_tuple():
    tuple1 = (1, 2, 3)
    assert type(tuple1) == tuple

def test_set():
    set1 = {1, 2, 3, 4, 5}
    assert type(set1) == set

def test_dict():
    dict1 = {"name": "John", "age": 30}
    assert type(dict1) == dict