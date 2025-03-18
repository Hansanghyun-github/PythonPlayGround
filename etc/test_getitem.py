

class Example:
    def __init__(self):
        self._list = [1, 2, 3]

    def __getitem__(self, index):
        return self._list[index]

class PrintExample:
    def __init__(self):
        self._list = [1, 2, 3]

    def __getitem__(self, index):
        return index

# [] operator is overloaded by __getitem__ method
def test_getitem():
    example = Example()
    assert example[0] == 1

def test_custom_getitem():
    print_example = PrintExample()
    assert print_example[0] == 0