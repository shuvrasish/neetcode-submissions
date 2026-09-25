# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            currentHas = False
            if node and node.val == subRoot.val:
                currentHas = self.isSameTree(node, subRoot)
            
            leftHas = dfs(node.left)
            rightHas = dfs(node.right)

            return leftHas or rightHas or currentHas
        
        return dfs(root)
        