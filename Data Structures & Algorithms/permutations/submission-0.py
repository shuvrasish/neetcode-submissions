class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        vis = set()
        sub = []
        def dfs() -> None:
            if len(sub) >= len(nums):
                res.append(sub[:])
                return
            
            for i in range(len(nums)):
                if i in vis:
                    continue
                vis.add(i)
                sub.append(nums[i])
                dfs()
                vis.remove(i)
                sub.pop()
        
        dfs()
        return res
