from abc import ABC, abstractmethod
from typing import Optional, Dict


class INode(ABC):
    @property
    @abstractmethod
    def next(self) -> Optional['INode']:
        ...

    @next.setter
    @abstractmethod
    def next(self) -> Optional['INode']:
        ...

    @property
    @abstractmethod
    def value(self) -> int:
        ...


class Node(INode):
    def __init__(self,
                 value: int,
                 next: Optional[INode] = None) -> None:
        self._next = next
        self._value = value

    @property
    def next(self) -> Optional[INode]:
        return self._next

    @next.setter
    def next(self, value: Optional[INode]) -> None:
        self._next = value

    @property
    def value(self) -> int:
        return self._value

    def __str__(self) -> str:
        _next = self.next.value if self.next else None
        return f"{self.value=} next={_next}"


def reverse_linked_list(head: INode) -> Optional[INode]:
    prev: Optional[INode] = None
    curr: Optional[INode] = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


n1, n2, n3 = Node(1), Node(2), Node(3)
n1._next, n2.next = n2, n3

lst = [n1, n2, n3]


def print_list():
    for i in (lst):
        print(i)


print_list()
print("*"*100)
print_list()
print("*"*100)
reverse_linked_list(n3)
print_list()


def singleton(class_: object) -> object:
    def getinstance(*args, **kwargs):
        if not getattr(class_, 'instance', None):
            class_.instance = class_(*args, **kwargs)
        return class_.instance
    return getinstance


@singleton
class Test:
    '''sdsds'''


class Singleton(type):
    _instances: Dict[str, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBProvider(metaclass=Singleton):
    pass
