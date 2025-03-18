# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        accum = Node(-1)
        prev = accum
        curr = None
        original = head
        map = {}
        while head:
            curr = Node(head.val)
            map[head] = curr
            if prev:
                prev.next = curr
            prev = prev.next
            head = head.next
        ptr = accum.next
        while original:
            if original.random in map:
                ptr.random = map[original.random]
            original = original.next
            ptr = ptr.next

        return accum.next
