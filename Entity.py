from typing import TypeVar, Generic

T = TypeVar('T')


class Entity(Generic[T]):
    """
    Key-value class (dictionary).
    """

    def __init__(self, key: T, val: T):
        self.__key = key
        self.__value = val

    @property
    def key(self) -> T:
        return self.__key

    @property
    def value(self) -> T:
        return self.__value

    @value.setter
    def value(self, val: T):
        self.__value = val

    def __str__(self):
        return '{} {}'.format(self.value, self.key)
