class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l][r] = True
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l][r] = True
                l -= 1
                r += 1

        def dfs(ind: int) -> None:
            if ind == len(s):
                res.append(path[:])
                return
            
            for i in range(ind, len(s)):
                if dp[ind][i]:
                    path.append(s[ind : i + 1])
                    dfs(i + 1)
                    path.pop()
        dfs(0)
        return res