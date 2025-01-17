class WithClass:
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')


def with_test():
    with WithClass():
        print('inside with block')

'''
Output:
enter
inside with block
exit
'''
with_test()
