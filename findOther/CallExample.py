def test_call_method_from_modele():
    from dir import ModuleExample
    assert ModuleExample.hello_world() == "Hello, World!"

def test_call_class_from_module():
    from dir import ModuleExample
    example = ModuleExample.Example("World")
    assert example.say_hello() == "Hello, World!"

def test_call_class_from_class():
    from dir.ClassExample import Example
    example = Example("World")
    assert example.say_hello() == "Hello, World!"
