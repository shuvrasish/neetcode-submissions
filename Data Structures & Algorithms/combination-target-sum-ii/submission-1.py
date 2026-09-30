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
            
            for ind in range(i, len(candidates)):
                if ind > i and candidates[ind - 1] == candidates[ind]:
                    continue
                if candidates[ind] + total > target:
                    break
                sub.append(candidates[ind])
                dfs(ind + 1, total + candidates[ind])
                sub.pop()
        
        dfs(0, 0)
        return res