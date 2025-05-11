from itertools import groupby

def test_groupby_with_sort():
    # given
    data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)]
    data.sort(key=lambda x: x[0])

    # when
    grouped = groupby(data, key=lambda x: x[0])

    # then
    for key, group in grouped:
        if key == "a":
            item_list = [item[1] for item in group]
            assert item_list == [1, 2, 5]
        elif key == "b":
            item_list = [item[1] for item in group]
            assert item_list == [3, 4]


def test_groupby_with_no_sort():
    # given
    data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)]
    # data.sort(key=lambda x: x[0])

    # when
    grouped = groupby(data, key=lambda x: x[0])

    # then
    for key, group in grouped:
        if key == "a":
            item_list = [item[1] for item in group]
            assert item_list == [1, 2] or item_list == [5]
        elif key == "b":
            item_list = [item[1] for item in group]
            assert item_list == [3, 4]


def test_groupby_with_value():
    # given
    data = [("a", 1), ("a", 1), ("b", 2), ("b", 2), ("a", 3)]

    # when
    grouped = groupby(data, key=lambda x: x[1])

    # then
    for key, group in grouped:
        if key == 1:
            item_list = [item[0] for item in group]
            assert item_list == ["a", "a"]
        elif key == 2:
            item_list = [item[0] for item in group]
            assert item_list == ["b", "b"]
        elif key == 3:
            item_list = [item[0] for item in group]
            assert item_list == ["a"]
