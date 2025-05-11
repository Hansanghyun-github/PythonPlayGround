def _test_method(num: int, name: str) -> None:  print(f"num: {num}, name: {name}")

def test_annotation():
    assert _test_method.__annotations__ == {'num': int, 'name': str, 'return': None}
