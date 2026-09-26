# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        pos = 1
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal ans
            nonlocal pos
            if not node:
                return
            dfs(node.left)
            if pos == k:
                ans = node.val
            pos += 1
            dfs(node.right)

        dfs(root)
        return ans
        
        