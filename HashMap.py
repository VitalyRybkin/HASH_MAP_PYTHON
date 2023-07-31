import copy
from typing import Type, TypeVar

from Bucket import Bucket
from Entity import Entity

T = TypeVar('T')

class HashMap:
    """
    Hash map class implements dictionary using hash function.
    """
    HASH_MAP_MAX_LOAD_FACTOR = 0.75
    HASH_MAP_MIN_LOAD_FACTOR = 0.30

    def __init__(self):
        self.__hash_map_capacity = 0
        self.__hash_map_size = 8
        self.__buckets = [None] * self.__hash_map_size
        self.__bucket = Bucket

    def __iter__(self):
        self.size = self.__hash_map_size - 1
        return self

    def __next__(self):
        if self.size < 0:
            raise StopIteration
        self.size -= 1
        return self.__buckets[self.size]

    @property
    def hash_map_size(self):
        return self.__hash_map_size

    @hash_map_size.setter
    def hash_map_size(self, val):
        self.__hash_map_size = val

    @property
    def hash_map_capacity(self):
        return self.__hash_map_capacity

    @hash_map_capacity.setter
    def hash_map_capacity(self, value):
        self.__hash_map_capacity = value

    @property
    def bucket(self) -> Type[Bucket]:
        return self.__bucket

    @property
    def buckets(self) -> list[None]:
        return self.__buckets

    @buckets.setter
    def buckets(self, buckets: list[None]):
        self.__buckets = copy.deepcopy(buckets)

    @classmethod
    def hash_code(cls, key, length) -> int:
        index: int = abs(hash(key) % length)
        return index

    def get(self, key: T) -> Entity | None:
        """
        Getting value from hash map dictionary by key.
        :param key: key to get value.
        :return: node from list of nodes.
        """
        index = self.hash_code(key, len(self.buckets))
        bucket: None = self.buckets[index]
        if bucket is None:
            print('No such key!')
            return
        return bucket.get_node(key)

    def put(self, key: T, val: T):
        """
        Adds element to hash map dictionary or updates existing.
        :param key: key of dictionary.
        :param val: value of dictionary.
        :return:
        """
        index = self.hash_code(key, len(self.buckets))
        bucket: None = self.buckets[index]
        if bucket is None:
            bucket: Bucket = Bucket()
            self.buckets[index] = bucket

        node_added = bucket.add_node(key, val)
        if node_added:
            self.hash_map_capacity += 1

        if self.hash_map_capacity > self.__hash_map_size * self.HASH_MAP_MAX_LOAD_FACTOR:
            print('Hash map resize is needed! Capacity:', self.hash_map_capacity)
            expand = True
            self.resize_hash_map(expand)

    def remove(self, key: T):
        """
        Removes element from hash map dictionary.
        :param key: Key to find removing element.
        :return:
        """
        bucket: None = self.buckets[self.hash_code(key, len(self.buckets))]
        if bucket is not None:
            node_removed = bucket.remove_node(key)
            if node_removed:
                self.hash_map_capacity -= 1

            if self.hash_map_capacity < self.__hash_map_size * self.HASH_MAP_MIN_LOAD_FACTOR:
                print('Hash map resize is needed! Capacity:', self.hash_map_capacity)
                expand = False
                self.resize_hash_map(expand)
        else:
            print('No such key!')

    def resize_hash_map(self, expand: bool):
        """
        Resizing hash map depending on max/min load factors.
        :param expand: Expanding/contract boolean parameter.
        :return:
        """
        if expand:
            self.hash_map_size *= 2
        else:
            self.hash_map_size = int(self.hash_map_size / 2)

        new_buckets = [None] * self.hash_map_size
        for item in self.buckets:
            if item is not None:
                current_head = item.head
                while current_head is not None:
                    index = self.hash_code(current_head.value.key, len(new_buckets))
                    new_bucket = new_buckets[index]
                    if new_bucket is None:
                        new_bucket: Bucket = Bucket()
                        new_buckets[index] = new_bucket

                    new_bucket.add_on_resize(current_head.value.key, current_head.value.value)
                    current_head = current_head.next

        self.buckets = new_buckets

    def print_all(self):
        """
        Printing hash map.
        :return:
        """
        for item in self:
            if item is not None:
                item.print_bucket()
