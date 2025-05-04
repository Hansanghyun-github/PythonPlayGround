
def test_zip_with_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 6]
    assert list(zip(list1, list2)) == [(1, 1), (2, 2), (3, 3), (4, 4), (5, 6)]

def test_zip_with_loop():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    result = []
    for a, b in zip(list1, list2):
        result.append(a + b)

    assert result == [2, 4, 6, 8, 10]

def test_zip_with_unmatched_length():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7]
    assert list(zip(list1, list2)) == [(1, 4), (2, 5), (3, 6)]
    # The last element of list2 is ignored