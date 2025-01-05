import pytest

def test_delete_value():
    num = 10
    del num
    with pytest.raises(NameError):
        print(num)

def test_delete_list():
    numbers = [1, 2, 3, 4, 5]
    del numbers[2]
    assert numbers == [1, 2, 4, 5]

def test_delete_list_with_slicing():
    numbers = [1, 2, 3, 4, 5]
    del numbers[1:3]
    assert numbers == [1, 4, 5]

def test_tuple_immutable():
    numbers = (1, 2, 3, 4, 5)
    with pytest.raises(TypeError):
        del numbers[2]

def test_delete_tuple():
    numbers = (1, 2, 3, 4, 5)
    del numbers
    with pytest.raises(NameError):
        print(numbers)

def test_delete_dict():
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    del numbers[2]
    assert numbers == {1: 'one', 3: 'three', 4: 'four', 5: 'five'}