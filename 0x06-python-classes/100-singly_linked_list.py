#!/usr/bin/python3

"""Defines a class Node and class SinglyLinkedList"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialization of a node of a singly linked list

        Args:
            data (int): An integer value as data of the node
            next_node : The next node of the singly linked list

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property attribute to retrieve the data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Instance attribute setter

        Args:
            value (int): Integer data of the node

        Raises:
            TypeError: If data is not an integer or node is not a node

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property attribute for retrieving the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the next_node

        Args:
            value: next node of the singly linked list

        Raises:
            TypeError: If next_node is not None or a node

        """
        if not isinstance(next_node, Node.next_node)
