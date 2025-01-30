from pydantic import BaseModel

class Child(BaseModel):
    b: int

    def __str__(self):
        return f'Child(b={self.b})'

class Parent(BaseModel):
    title: str
    child: Child

    def __str__(self):
        return f'Parent(title={self.title}, child={self.child})'


def test_dict_type():
    parent: Parent = Parent(title='제목', child=Child(b=2))

    assert type(parent.child) == Child
    assert type(parent.dict()['child']) == dict