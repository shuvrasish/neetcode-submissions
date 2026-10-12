class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pcf, atl = set(), set()

        def dfs(r: int, c: int, visited: set, prev: int):
            if r < 0 or c < 0 or r >= m or c >= n or (r,c) in visited or heights[r][c] < prev:
                return
            
            visited.add((r,c))
                    
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])

        for col in range(n):
            dfs(0, col, pcf, heights[0][col])
            dfs(m - 1, col, atl, heights[m - 1][col])

        for row in range(m):
            dfs(row, 0, pcf, heights[row][0])
            dfs(row, n - 1, atl, heights[row][n - 1])

        ans = []
        for r in range(m):
            for c in range(n):
                if (r,c) in atl and (r, c) in pcf:
                    ans.append([r, c])
        
        return ans

