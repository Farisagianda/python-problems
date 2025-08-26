"""
🧩 Problem: Detect a Cycle in a Linked List
Goal:
Given the head of a linked list, determine if the linked list contains a cycle.

A cycle exists if any node can be reached again by continuously following the next pointer.

Example 1 — Cycle Exists
10 → 20 → 30
      ↑    ↓
      └────┘
Output: True

Example 2 — No Cycle
10 → 20 → 30 → None
Output: False

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def isCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head
        while fast:
            print(f"FAST: {fast.val}")
            print(f"SLOW: {slow.val}")
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = head.next.next
ll = LinkedList()
print(ll.isCycle(head))