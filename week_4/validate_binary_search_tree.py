# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bst = self.isValidBSTHelper(root)
        return bst[0]
    
    def isValidBSTHelper(self, root):
        # only if the input is None
        if root == None:
            return [True, None, None]
        # leaf will hit this case
        if root.left == None and root.right == None:
            return [True, root.val, root.val]
        left = [None, root.val, root.val]
        if root.left:
            left = self.isValidBSTHelper(root.left)
            if not left[0] or (left[2] >= root.val):
                return [False, None, None]
            else:
                left = [True, left[1], root.val]
            

        right = [None, root.val, root.val]
        if root.right:
            # check right is ValidBST, make sure that the maximum of right branch is smaller 
            # than current
            right = self.isValidBSTHelper(root.right)
            if not right[0] or (right[1] <= root.val):
                return [False, None, None]
            else:
                right = [True, root.val, right[2]]
        
        return [True, left[1], right[2]]