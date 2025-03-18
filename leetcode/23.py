# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = []
        nonEmptyCount = 0
        for ll in lists:
            if ll:
                nonEmptyCount += 1
        for ll in lists:
            if ll:
                heads.append(ll) # linked-list of heads
                nonEmptyCount += 1
        
        result = ListNode()
        head = result
        while nonEmptyCount > 1:
            nonEmptyCount = 0
            smallest = -1
            for i in range(len(lists)):
                curr_head = lists[i]
                if curr_head:
                    nonEmptyCount += 1
                    if smallest == -1:
                        smallest = i
                    elif curr_head.val < lists[smallest].val:
                        smallest = i
            head.next = lists[smallest]
            head = head.next
            lists[smallest] = lists[smallest].next
        
        for i in range(len(lists)):
            curr_head = lists[i]
            while curr_head:
                head.next = curr_head
                head = head.next
                curr_head = curr_head.next
        return result.next