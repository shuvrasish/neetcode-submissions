# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0

            maxl = helper(root.left)
            maxr = helper(root.right)

            res = max(res, maxl + maxr + 1)

            return 1 + max(maxl, maxr)
        helper(root)
        return res - 1
        
