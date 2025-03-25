# 114. Flatten Binary Tree to Linked List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        self.flatten(root.left) # flatten the left subtree
        self.flatten(root.right) # flatten the right subtree
        right_subtree = root.right
        root.right = root.left
        root.left = None
        while root and root.right:
            root = root.right
        root.right = right_subtree
