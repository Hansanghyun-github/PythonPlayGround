import pytest

def test_filter1():
    # given
    list1 = [1, 2, 3, 4, 5]

    # when
    result = list(filter(lambda x: x % 2 == 0, list1))
    # filter({lambda method}, {list})

    # then
    assert result == [2, 4]

def test_filter2():
    # given
    list1 = [1, 2, 3, 4, 5]

    # when
    result = filter(lambda x: x % 2 == 0, list1)
    # filter({lambda method}, {list})

    # then
    assert result.__next__() == 2
    assert result.__next__() == 4
    with pytest.raises(StopIteration):
        result.__next__()