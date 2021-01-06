#!/usr/bin/python3
'''Single linked list: linked list class'''


class Node:
    '''New Node'''

    def __init__(self, data, next_node=None):
        '''create a node'''

        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            '''return private attribute'''
            return self.__data

        @data.setter
        def data(self, value):
            '''asign value to data'''
            if type(value) is not int:
                raise TypeError('data must be an integer')
            self.__data = value

        @property
        def next_node(self):
            '''return private attribute next node'''
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            '''asign value to attribute'''
            if type(value) is not object and type(value) is not None:
                raise TypeError('next_node must be a node object')
            self.__next_node = value

class SinglyLinkedList:
    '''Linked list class'''

    def __init__(self):
        '''new instance of singly linked list'''
        self.head = None

    def __str__(self):
        '''print all the linked list'''
        temp = self.head
        new = ""
        while(temp):
            new += str(temp.data)
            if temp.next_node is not None:
                new += "\n"
            temp = temp.next_node
        return new

    def sorted_insert(self, value):
        '''sort the new node'''
        new_node = Node(value)
        if self.head is None:
            new_node.next_node = self.head
            self.head = new_node

        elif self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while(current.next_node is not None and
                current.next_node.data < new_node.data):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
