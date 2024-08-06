# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = preorder[0]
        preorder = preorder[1::]

        cut = inorder.index(root)
        left_inorder = inorder[0:cut]
        right_inorder = inorder[cut+1::]
        left_preorder = preorder[0:len(left_inorder)]
        right_preorder = preorder[len(left_inorder)::]

        left = self.buildTree(left_preorder, left_inorder)
        right = self.buildTree(right_preorder, right_inorder)

        return TreeNode(root, left, right)
        


        
