class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        l = len(word)

        def dfs(i: int, j: int, k:int) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n or k >= l:
                return False
            
            if board[i][j] == '-' or board[i][j] != word[k]:
                return False
            
            if k == l - 1:
                return True

            original = board[i][j]
            # set this as "-"
            board[i][j] = "-"
            # search for next char in all dirs
            found = (
                dfs(i - 1, j, k + 1) or 
                dfs(i + 1, j, k + 1) or 
                dfs(i, j - 1, k + 1) or 
                dfs(i, j + 1, k + 1)
            )
            # reset to original char
            board[i][j] = original
            return found

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(i, j, 0):
                    return True
        
        return False

