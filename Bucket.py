from typing import Type, TypeVar

from Entity import Entity

T = TypeVar('T')


class Bucket:
    """
    Linked list of dictionary (key-value) elements.
    """
    def __init__(self):
        self.__head = self.__tail = None
        self.__entity = Entity
        self.__node = self.Node

    def __iter__(self):
        self.print_node = self.head
        return self

    def __next__(self):
        if self.print_node is None:
            raise StopIteration

        result = self.print_node
        self.print_node = self.print_node.next

        return result

    class Node:
        """
        Node of linked list (bucket).
        """
        def __init__(self, val: Entity = None):
            self.__next = None
            self.__value = val

        @property
        def value(self) -> Entity:
            return self.__value

        @property
        def next(self) -> None:
            return self.__next

        @next.setter
        def next(self, node):
            self.__next = node

    @property
    def entity(self):
        return self.__entity

    @property
    def node(self) -> Type[Node]:
        return self.__node

    @property
    def head(self) -> Node:
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @property
    def tail(self) -> Node:
        return self.__tail

    @tail.setter
    def tail(self, node):
        self.__tail = node

    def add_entity(self, key: T, val: T) -> Node:
        """
        Creating a node of linked list (key-value element and next element) to a linked list of nodes.
        :param key: key to add to dictionary.
        :param val: value to add to dictionary.
        :return: new node of linked list
        """
        entity: Entity = self.entity(key, val)
        node = self.node(entity)
        return node

    def add_node(self, key: T, val: T) -> bool:
        """
        Adding a node (key-value element and next element) to a linked list or updating an existing node.
        :param key: key to add to dictionary.
        :param val: value to add to dictionary.
        :return:
        """
        node = self.add_entity(key, val)
        if self.head is None:
            self.head = self.tail = node
            print('Added:', self.head.value)
            return True

        current_node = self.head
        while current_node is not None:
            if current_node.value.key == key:
                current_node.value.value = val
                return False
            if current_node.next is None:
                self.tail.next = node
                self.tail = self.tail.next
                print('Added:', self.tail.value)
                return True
            current_node = current_node.next

    def add_on_resize(self, key: T, val: T):
        """
        Adding a node to a new linked list.
        :param key: key to add to dictionary.
        :param val: value to add to dictionary.
        :return:
        """
        node = self.add_entity(key, val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def remove_node(self, key) -> bool:
        """
        Removing a node (key-value element and next element) from a linked list.
        :param key:
        :return:
        """
        if self.head is None:
            print('No such key!')
            return False
        if self.head.value.key == key:
            print('Removed:', self.head.value)
            self.head = self.head.next
            return True
        if self.head.next is not None:
            current_node = prev = self.head
            current_node = current_node.next
            while current_node is not None:
                if current_node.value.key == key:
                    print('Removed:', current_node.value)
                    prev.next = current_node.next
                    return True
                current_node = current_node.next
            print('No such key!')

        return False

    def get_node(self, key) -> Entity | None:
        """
        Getting a value from key-value element by key.
        :param key: key to get value.
        :return: key-value element
        """
        if self.head is None:
            print('No such key!')
            return
        if self.head.value.key == key:
            return self.head.value
        current_node = self.head
        while current_node is not None:
            if current_node.value.key == key:
                return current_node.value
            current_node = current_node.next

        print('No such key!')

    def print_bucket(self):
        """
        Print linked list of key-value elements.
        """
        for item in self:
            print(item.value)
