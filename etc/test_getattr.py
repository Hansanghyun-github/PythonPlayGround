import pytest

class Example:
    def __init__(self, value):
        self.attribute = value

def test_getattr():
    obj = Example('Hello')

    # getattr({object}, {field})
    value = getattr(obj, 'attribute')
    assert value == 'Hello'

    # getattr({object}, {field}, {default_value})
    default_value = getattr(obj, 'non_existent', 'Default Value')
    assert default_value == 'Default Value'

def test_getattr2():
    obj = Example('Hello')

    with pytest.raises(AttributeError):
        value = getattr(obj, 'unknown')