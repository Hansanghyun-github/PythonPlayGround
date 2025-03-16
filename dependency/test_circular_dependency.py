import pytest

def test_filter1():
    with pytest.raises(ImportError):
        from dependency.class2 import B # error
        b = B()