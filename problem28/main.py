#!/usr/local/bin/python3

"""
🧩 Problem: Find the Length of a Linked List

    Goal: Given the head of a singly linked list, return the number of nodes in it.

✅ Example

If the linked list is:

1 → 2 → 3 → 4 → None

Then the answer is 4.
💡 Why it’s a good starter:

    No pointer manipulation.

    Just a loop and a counter.

    Helps you get comfortable with the structure of a linked list.
"""

class linklist:
  def __init__(self):
    pass
  
  def checklength(self, head):
    count = 0
    current = head
    while current:
      count += 1
      current = current.next
    return count
