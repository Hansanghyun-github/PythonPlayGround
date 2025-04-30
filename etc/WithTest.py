class WithClass:
    def __init__(self):
        self.value = 1
    def __enter__(self):
        self.value += 2
    def __exit__(self, exc_type, exc_value, traceback):
        self.value += 3


def test_with_block():
    target = WithClass()
    with target:
        print('inside with block')

    assert target.value == 6

def test_with_block_with_error():
    target = WithClass()
    try:
        with target:
            raise Exception('test exception')
    except Exception as e:
        print('exception:', e)

    assert target.value == 6
    # if error is occurred, __exit__ method will be called
