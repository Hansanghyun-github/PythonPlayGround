# Example of list comprehension
def test_list_comprehension():
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    assert squares == [1, 4, 9, 16, 25]

# Example of dictionary comprehension
def test_dict_comprehension():
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    my_dict = {k: v for k, v in zip(keys, values)}
    assert my_dict == {'a': 1, 'b': 2, 'c': 3, 'd': 4}