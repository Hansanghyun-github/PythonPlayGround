from dependency.class2 import C


class A:
    def __init__(self):
        self.num = C().get_num()

    def get_num(self) -> int:
        return self.num
