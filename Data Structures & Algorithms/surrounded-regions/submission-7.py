class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        if m <= 2 or n <= 2:
            return

        def dfs(r: int, c: int) -> bool:
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            if board[r][c] == 'X' or board[r][c] == "Y":
                return True
            
            # print(f"r={r}, c={c}, board[r][c]={board[r][c]}")
            
            board[r][c] = "Y"

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            poss = True
            for dr, dc in dirs:
                if not dfs(r + dr, c + dc):
                    poss = False
            return poss

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = "X"
                elif board[r][c] == "Y":
                    board[r][c] = "O"
        