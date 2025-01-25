from unittest import mock

class SampleClass:
    def print_value(self):
        print('Real Class')

def test_mocking():
    sample = SampleClass()
    sample.print_value = mock.Mock(return_value='Mocked Class')
    assert sample.print_value() == 'Mocked Class'

