# 86. Partition List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessNode = ListNode(-1)
        first = lessNode
        greaterNode = ListNode(-1)
        second = greaterNode
        while head:
            print(head.val)
            if head.val < x:
                lessNode.next = head
                lessNode = lessNode.next
            else:
                greaterNode.next = head
                greaterNode = greaterNode.next
            head = head.next
        lessNode.next = second.next
        greaterNode.next = None # need to terminate this otherwise it would be memory limit exceeded
        return first.next