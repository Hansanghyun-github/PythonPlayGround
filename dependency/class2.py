from dependency.class1 import A


class B:
    def __init__(self):
        self.a = A()

    def print(self):
        print(self.a.get_num())

class C:
    def __init__(self):
        self.num = 5

    def get_num(self) -> int:
        return self.num
