

class MyList:
    def __init__(self):
        self._list = [1, 2, 3]

    def __getitem__(self, index):
        return self._list[index]

class CustomMyList:
    def __init__(self):
        self._list = [1, 2, 3]

    def __getitem__(self, index):
        return index

class PrintMyList:
    def __init__(self):
        self._list = [1, 2, 3]

    def __getitem__(self, index):
        print(index)
        return self._list[index]

class MyList2:
    def __init__(self):
        self._list = [1, 2, 3]

    def __getitem__(self, index):
        return self._list[index]

    def __contains__(self, item):
        print(item)
        return item in self._list


# [] operator is overloaded by __getitem__ method
def test_getitem():
    my_list = MyList()
    assert my_list[0] == 1

def test_custom_getitem():
    custom_my_list = CustomMyList()
    assert custom_my_list[0] == 0

def test_custom_getitem_2():
    my_list = MyList()
    assert my_list[1:2] == [2]

    custom_my_list = CustomMyList()
    assert custom_my_list[1:2] == slice(1, 2, None)
    # index slicing send slice object to __getitem__ method

    assert my_list.__getitem__(slice(0,1)) == [1]

def test_contains():
    my_list_2 = MyList2()
    assert 1 in my_list_2 # prints 1
    assert 2 in my_list_2 # prints 2
    # in operator is overloaded by __contains__ method

def test_contains_2():
    print_my_list = PrintMyList()
    assert 1 in print_my_list # prints 0
    assert 2 in print_my_list # prints 0, 1
    # if __contains__ method is not defined, __getitem__ method is called for each element in the list