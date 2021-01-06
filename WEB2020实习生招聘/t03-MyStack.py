# python3

# 可以选择其它语言实现
# 1. 自己实现一个先进后出的栈 MyStack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyStack():
    """
    # 不可使用内置标准类 list
    # 实现和list同样功能的实例方法 append, remove, pop，index, __len__, __eq__, __str__
    """

    def __init__(self, *args):
        self.arg = [*args]

    def append(self, x):
        pass

    def remove(self, x):
        pass

    def pop(self):
        pass

    def index(self, x):
        pass

    def __len__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass


def test_my_stack():
    a = MyStack(1, 2, 3)
    assert len(a) == 3

    x = a.pop()
    assert x == 3

    a.append(4)
    print(a)
    # [1, 2, 4]

    a.remove(2)
    print(a)
    # [1, 4]

    i = a.index(4)
    assert i == 2

    b = MyStack(1, 4)
    c = MyStack(4, 1)
    assert a == b
    assert b != c
