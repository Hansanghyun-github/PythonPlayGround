class WithClass:
    def __init__(self):
        self.value = 1
    def __enter__(self):
        self.value += 10
    def __exit__(self, exc_type, exc_value, traceback):
        self.value += 100
        print('exit:', exc_type, exc_value, traceback)


def test_with_block():
    target = WithClass()
    with target:
        print('inside with block')

    assert target.value == 111

def test_with_block_with_error():
    target = WithClass()
    try:
        with target:
            print('inside with block')
            raise Exception('test exception')
    except Exception as e:
        print('exception:', e)

    assert target.value == 111
    # if error is occurred, __exit__ method will be called
