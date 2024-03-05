"""
Doing a linked list in Python is a little goofy, but what is experimentation but goofy acts
taken seriously?

Iteration is O(n), insertion is O(1)
"""
from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def set_pointer(self, node) -> None:
        self.next = node


# Since there's no memory management tom-foolery, we can implement straight away.
n1 = Node(1, None)
n2 = Node(2, None)
n3 = Node(3, None)
n4 = Node(4, None)

n1.set_pointer(n2)
n2.set_pointer(n3)
n3.set_pointer(n4)

# Iterating the linked list
x = n1
while True:
    print(x.data)
    if x.next is None:
        break
    x = x.next

