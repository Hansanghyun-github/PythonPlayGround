import pytest

def test_list_size():
    # when
    ll: list[int] = [1, 2, 3, 4, 5]

    # then
    assert len(ll) == 5
    assert ((not ll) == False)

def test_list_size_is_zero():
    # when
    ll: list[int] = []

    # then
    assert len(ll) == 0
    assert ll is not None
    assert ((not ll) == True)

def test_list_is_none():
    # when
    ll: list[int] = None

    # then
    assert ll is None
    assert ((not ll) == True)
    with pytest.raises(TypeError):
        assert len(ll) == 0
