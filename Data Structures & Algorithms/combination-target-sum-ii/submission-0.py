class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        candidates.sort()

        def dfs(i: int, total: int) -> None:
            if total == target:
                res.append(sub[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            sub.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            sub.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            dfs(i + 1, total)
        
        dfs(0, 0)
        return res