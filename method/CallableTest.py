def sample_method():
    pass

class SampleClass:
    pass

def test_method_is_callable():
    assert callable(sample_method) == True

def test_variable_is_not_callable():
    a = 1
    assert callable(a) == False

def test_class_is_callable():
    assert callable(SampleClass) == True

def test_instance_is_not_callable():
    sample_instance = SampleClass()
    assert callable(sample_instance) == False
