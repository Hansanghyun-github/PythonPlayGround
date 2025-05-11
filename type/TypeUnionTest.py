from typing import Union

def sample_method(x: Union[int, str]):
    print(x)

def test_union_type():
    # no error
    sample_method(5)
    sample_method("hello")

def sample_method2(x: int | str):
    print(x)

def test_union_type2():
    # no error
    sample_method2(5)
    sample_method2("hello")
