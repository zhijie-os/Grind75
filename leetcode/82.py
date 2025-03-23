# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        acc = result

        while head:
            val = head.val
            print(val)
            curr = head
            # if it is duplicate 
            if head.next and head.next.val == val:
                print(val, head.next.val)
                # discard all values that are the same
                while head and head.val == val:
                    head = head.next
            else:
                print("attaching ", head.val, " to ", acc.val)
                acc.next = head
                acc = acc.next
                head = head.next
        acc.next = None
        return result.next
