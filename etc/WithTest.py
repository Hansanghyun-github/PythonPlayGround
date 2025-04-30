class WithClass:
    def __init__(self):
        self.value = 1
    def __enter__(self):
        self.value += 2
    def __exit__(self, exc_type, exc_value, traceback):
        self.value += 3


def test_with():
    target = WithClass()
    with target:
        print('inside with block')

    assert target.value == 6
