def test_sorted():
    list = [3, 1, 2, 5, 4]
    result = sorted(list)
    assert result == [1, 2, 3, 4, 5]

def test_sorted_with_lambda():
    list = [3, 1, 2, 5, 4]
    result = sorted(list, key=lambda x: x % 2 == 0)
    assert result == [3, 1, 5, 2, 4]

def test_sorted_with_lambda_reverse():
    list = [3, 1, 2, 5, 4]
    result = sorted(list, key=lambda x: x % 2 == 0, reverse=True)
    assert result == [2, 4, 3, 1, 5]
