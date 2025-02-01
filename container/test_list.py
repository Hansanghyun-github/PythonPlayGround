import pytest

def test_list_size():
    ll: list[int] = [1, 2, 3, 4, 5]
    assert len(ll) == 5

def test_list_size_is_zero():
    ll: list[int] = []
    assert len(ll) == 0
    assert ll is not None

def test_list_is_none():
    ll: list[int] = None
    assert ll is None
    with pytest.raises(TypeError):
        assert len(ll) == 0