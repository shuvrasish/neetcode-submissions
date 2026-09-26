# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lastEl = float('-inf')

        def inorder(node: Optional[TreeNode]) -> bool:
            nonlocal lastEl
            if not node:
                return True
            currentValid = True
            leftValid = inorder(node.left)
            if node.val <= lastEl:
                currentValid = False
            lastEl = node.val
            rightValid = inorder(node.right)
            return leftValid and currentValid and rightValid

        return inorder(root)