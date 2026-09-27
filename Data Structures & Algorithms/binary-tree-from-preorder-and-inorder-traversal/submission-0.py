class Solution:
    def buildTree(self, preorder, inorder):
        n = len(preorder)
        inorderDict = {}

        for i, val in enumerate(inorder):
            inorderDict[val] = i

        def buildTreeHelper(pi, pj, ii, ij):
            if pi > pj or ii > ij:
                return None

            currHead = TreeNode(preorder[pi]) 
            ih = inorderDict[preorder[pi]] 

            leftSize = ih - ii

            currHead.left = buildTreeHelper(pi + 1, pi + leftSize, ii, ih - 1) 
            currHead.right = buildTreeHelper(pi + leftSize + 1, pj, ih + 1, ij) 
            return currHead

        return buildTreeHelper(
            0,
            n - 1,
            0,
            n - 1
        )