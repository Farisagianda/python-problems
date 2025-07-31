#!/usr/local/bin/python3

"""
🧩 Problem: Find the Middle of a Linked List

Goal:
Given the head of a singly linked list, return the value of the middle node.

If there are two middle nodes (even number of nodes), return the second one.
✅ Example:

Input: 10 → 20 → 30  
Output: 20

Input: 10 → 20 → 30 → 40  
Output: 30  # second middle
"""

class LinkedList:
  def middleLinkList(self, head):
     current = head
     pointerA, pointerB = current, current
     while pointerB:
       pointerA = pointerA.next
       pointerB = pointerB.next.next
     print(pointerA.val)
     return pointerA.val

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

ll = LinkedList()
print(ll.middleLinkList(head))
