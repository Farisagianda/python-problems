#!/usr/local/bin/python3

"""
🧩 Problem: Count the Number of Nodes in a Linked List

Goal:
Write a function to count how many nodes are in a singly linked list.
✅ Example:

Given this linked list:

[10] → [20] → [30] → None

Your function should return:

3
"""

class LinkedList:
  def checknode(self, head):
    counter = 0
    current = head
    while current:
      counter += 1
      current = current.next
    return counter

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
ll = LinkedList()
print(ll.checknode(head))
