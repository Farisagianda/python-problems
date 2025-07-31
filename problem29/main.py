#!/usr/local/bin/python3

"""


Task:
Write a function that takes the head of a singly linked list and returns the value of the last node.
✅ Example:

Given the linked list:

head → 10 → 20 → 30 → None

Your function should return: 30
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def lastnode(self, head):
    current = head
    while current:
       if not current.next:
          return current.val
       current = current.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(4)

ll = LinkedList()
print(ll.lastnode(head))
