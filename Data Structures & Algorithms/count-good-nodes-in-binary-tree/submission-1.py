# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node: TreeNode, maxInPath: int) -> None:
            nonlocal count
            if not node:
                return
            
            if node.val >= maxInPath:
                maxInPath = node.val
                print(node.val)
                count += 1
            
            dfs(node.left, maxInPath)
            dfs(node.right, maxInPath)

        dfs(root, -101)
        return count


