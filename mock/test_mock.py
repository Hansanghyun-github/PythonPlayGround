from unittest import mock

import pytest

class SampleClass:
    def print_value(self) -> str:
        return 'Real Class'

def test_mocking_method():
    sample = SampleClass()
    sample.print_value = mock.Mock(return_value='Mocked Class')
    assert sample.print_value() == 'Mocked Class'

def test_mocking_object_call():
    sample = mock.Mock()
    sample.print_value()
    sample.print_value.assert_called_once()

def test_mocking_object_not_call():
    sample = mock.Mock()
    with pytest.raises(AssertionError):
        sample.print_value.assert_called_once()

