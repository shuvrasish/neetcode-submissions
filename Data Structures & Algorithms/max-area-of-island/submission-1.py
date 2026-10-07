class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i: int, j: int) -> int:
            nonlocal res
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            dirs = [
                (-1, 0), (1, 0), (0, 1), (0, -1)
            ]

            for dx, dy in dirs:
                area += dfs(i + dx, j + dy)
            
            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res