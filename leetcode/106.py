# 106. Construct Binary Tree from Inorder 
# and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base case
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1]) #
        leftIn = inorder[0:inorder.index(postorder[-1])]
        leftPost = postorder[0:len(leftIn)]
        rightIn = inorder[inorder.index(postorder[-1])+1:]
        rightPost = postorder[len(leftIn):len(leftIn)+len(rightIn)]

        left = self.buildTree(leftIn, leftPost)
        right = self.buildTree(rightIn, rightPost)
        root.left = left
        root.right = right
        return root