class Solution:

    
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            # Odd-length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l][r] = True
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l][r] = True
                l -= 1
                r += 1

        def dfs(ind: int) -> None:
            if ind == n:
                res.append(path[:])
                return

            for j in range(ind, n):
                if dp[ind][j]:
                    path.append(s[ind:j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return res