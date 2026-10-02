class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res, sub = [], []
        
        def dfs(ind: int) -> None:
            if ind >= len(nums):
                res.append(sub[:])
                return
            
            # take
            sub.append(nums[ind])
            dfs(ind + 1)
            sub.pop()

            while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1

            # not take
            dfs(ind + 1)

        dfs(0)
        return res