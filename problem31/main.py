#!/usr/local/bin/python3

"""
🔁 Problem: Reverse a Linked List

🧠 Goal: Given a singly linked list, reverse the list so the nodes point in the opposite direction.

Input:

1 → 2 → 3 → 4 → None

Output:

4 → 3 → 2 → 1 → None

"""

class LinkedList:
  def reverselist(self, head):
    prev = None
    current = head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    return prev

class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

ll = LinkedList()
reverse_head = ll.reverselist(head)
while reverse_head:
  print(reverse_head.val)
  reverse_head = reverse_head.next
