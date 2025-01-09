from typing import Tuple

def invariable_method(args: Tuple[int, ...]): # int형 데이터를 가진 튜플만 받을 수 있음
    print(args)

def test_method():
    invariable_method((1, 2, 3, 4, 5))

    invariable_method(("str")) 
    # type hinting에 맞지 않는 데이터를 넣어도 에러가 발생하지 않음
    # type hinting은 문서 역할을 하기 때문에 코드 실행에는 영향을 주지 않음