import pytest
from collections import defaultdict

def test_dict_not_found():
    # given
    dict: dict[str, int] = {}

    # when # then
    with pytest.raises(KeyError):
        dict['key']

def test_dict_defaultdict_not_found():
    # given
    dict: defaultdict[str, int] = defaultdict(int)

    # when
    value = dict['key']

    # then
    assert value == 0

def test_dict_defaultdict_not_found_str():
    # given
    dict: defaultdict[str, str] = defaultdict(str)

    # when
    value = dict['key']

    # then
    assert value == ''


def test_dict_defaultdict_None():
    # given
    dic: dict[str, str] = {}
    dic[None] = 'value'

    # when
    value = dic[None]

    # then
    print(value)

