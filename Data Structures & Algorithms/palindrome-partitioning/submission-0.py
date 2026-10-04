class Solution:
    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        i, j = start, end

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def dfs(ind: int) -> None:
            if ind == len(s):
                res.append(path[:])
                return
            
            for i in range(ind, len(s)):
                if self.isPalindrome(s, ind, i):
                    path.append(s[ind : i + 1])
                    dfs(i + 1)
                    path.pop()
        dfs(0)
        return res