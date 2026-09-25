# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            sz = len(q)

            sub = []
            while sz:
                el = q.popleft()
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
                sub.append(el.val)
                sz -= 1
            res.append(sub)
        
        return res