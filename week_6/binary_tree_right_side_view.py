# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        #BFS implementation.
        while q:
            r_side = None
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node:
                    r_side = node
                    q.append(node.left)
                    q.append(node.right)
            if r_side:
                res.append(r_side.val)
            
        return res