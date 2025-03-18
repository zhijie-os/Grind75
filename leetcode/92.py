# 92. Reverse Linked List II
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        totalHead = head
        leftLast = None
        rightFirst = None
        dummy = ListNode()
        reversedHead = None
        reversedTail = None
        i = 1

        while head != None:
            if i == left - 1:
                leftLast = head
            if i == right + 1:
                rightFirst = head
            if i>= left and i <= right:
                next = head.next
                head.next = dummy.next
                if dummy.next == None:
                    reversedTail = head
                dummy.next = head
                head = next
                reversedHead = dummy.next
            else:
                head = head.next
            i += 1
        
        if leftLast:
            leftLast.next = reversedHead
        else:
            totalHead = reversedHead
        if rightFirst:
            reversedTail.next = rightFirst

        return totalHead