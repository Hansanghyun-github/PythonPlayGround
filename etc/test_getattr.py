class Example:
    def __init__(self, value):
        self.attribute = value

def test_getattr():
    obj = Example('Hello')

    # 'attribute' 속성의 값을 가져옵니다
    value = getattr(obj, 'attribute')
    assert value == 'Hello'

    # 존재하지 않는 속성을 기본값과 함께 가져옵니다
    # getattr({object}, {field}, {default_value})
    default_value = getattr(obj, 'non_existent', 'Default Value')
    assert default_value == 'Default Value'
