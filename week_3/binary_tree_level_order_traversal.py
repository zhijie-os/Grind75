# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root,1)]
        res = []
        arr = []
        level = 1
        while len(queue) > 0:
            curr = queue[0]
            queue.pop(0)
            if curr[1] == level:
                arr.append(curr[0].val)
            else:
                level += 1
                res.append(arr)
                arr = [curr[0].val]
            if curr[0].left:
                queue.append((curr[0].left, level+1))
            if curr[0].right:
                queue.append((curr[0].right, level+1))
        res.append(arr)
        return res
