class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])

        freshCount = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        time = 0
        while q and freshCount:
            sz = len(q)
            while sz:
                r, c = q.popleft()
                sz -= 1
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshCount -= 1
                        q.append((nr, nc))
            time += 1
        
        return -1 if freshCount else time

