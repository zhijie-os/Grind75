# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        tail = None
        while ptr:
            length += 1
            tail = ptr
            ptr = ptr.next
        if length == 0:
            return head
        k %= length
        if k == 0:
            return head

        ptr = head
        prev = None
        for i in range(length - k):
            prev = ptr
            ptr = ptr.next
        
        prev.next = None
        tail.next = head
        return ptr
        

