import pytest

class Example:
    def __init__(self, value):
        self.attribute = value

def test_getattr():
    # given
    obj = Example('Hello')

    # when
    value = getattr(obj, 'attribute')

    # then
    assert value == 'Hello'

def test_getattr_unknown_attribute():
    # given
    obj = Example('Hello')

    # when # then
    with pytest.raises(AttributeError):
        value = getattr(obj, 'unknown')



def test_getattr_default():
    # given
    obj = Example('Hello')

    # when
    default_value = getattr(obj, 'non_existent', 'Default Value')

    # then
    assert default_value == 'Default Value'
