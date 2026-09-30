class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i: int, total: int) -> None:
            if total == target:
                res.append(sub[:])
                return
            if i >= len(nums) or total > target:
                return
            
            sub.append(nums[i])
            dfs(i, total + nums[i])
            sub.pop()

            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
