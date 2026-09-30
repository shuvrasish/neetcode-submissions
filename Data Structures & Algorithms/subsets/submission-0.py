class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i: int, sub: List[int]) -> None:
            if i >= len(nums):
                res.append(sub[:])
                return
            not_take = backtrack(i + 1, sub)
            sub.append(nums[i])
            take = backtrack(i + 1, sub)
            sub.pop()
        backtrack(0, [])
        
        return res