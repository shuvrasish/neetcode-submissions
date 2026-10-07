class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        res = 0
        def dfs(i: int, j: int) -> None:
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dirs = [
                (-1, 0), (1, 0), (0, 1), (0, -1)
            ]

            for dx, dy in dirs:
                dfs(i + dx, j + dy)
            

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res
