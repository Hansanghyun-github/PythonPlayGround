from unittest import mock

import pytest

class SampleClass:
    def print_value(self) -> str:
        return 'Real Class'

    @staticmethod
    def print_static_value() -> str:
        return 'Real Static Class'

def test_mocking_method():
    # given
    sample = SampleClass()

    # when
    sample.print_value = mock.Mock(return_value='Mocked Class')

    # then
    assert sample.print_value() == 'Mocked Class'

def test_mocking_static_method():
    # given
    SampleClass.print_static_value = mock.Mock(return_value='Mocked Static Class')

    # when
    return_value = SampleClass.print_static_value()

    # then
    assert return_value == 'Mocked Static Class'
    SampleClass.print_static_value.assert_called_once()

def test_mocking_object_call():
    # given
    sample = mock.Mock()

    # when
    sample.print_value()

    # then
    sample.print_value.assert_called_once()

def test_mocking_object_not_call():
    # given
    sample = mock.Mock()

    # when # then
    with pytest.raises(AssertionError):
        sample.print_value.assert_called_once()

