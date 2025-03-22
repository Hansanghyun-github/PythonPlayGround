from dir import ModuleExample

def test_call_method_from_modele():
    assert ModuleExample.hello_world() == "Hello, World!"

def test_call_class_from_module():
    example = ModuleExample.Example("World")
    assert example.say_hello() == "Hello, World!"

from dir.ClassExample import Example

def test_call_class_from_class():
    example = Example("World")
    assert example.say_hello() == "Hello, World!"