# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def helper(root) -> int:
            nonlocal isBalanced

            if not root:
                return 0
            lefth = helper(root.left)
            righth = helper(root.right)

            if isBalanced:
                isBalanced = (abs(lefth - righth) <= 1)
            
            return 1 + max(lefth, righth)

        helper(root)
        
        return isBalanced