# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        # O(1) memory space
        totalHead = ListNode()
        curr = None
        i = 1
        prevTail = totalHead
        nextTail = None
        while head != None:
            if i % k == 1:
                def hasEnough(head, k):
                    if k == 0:
                        return True
                    if head:
                        return hasEnough(head.next, k-1)
                    else:
                        return False

                if not hasEnough(head, k):
                    prevTail.next = head
                    return totalHead.next
                curr = ListNode()
                nextTail = head
            # do it either way
            next = head.next
            head.next = curr.next

            curr.next = head
            head = next
            if i % k == 0: # end of an reversion
                prevTail.next = curr.next
                prevTail = nextTail
            i += 1
                

        return totalHead.next