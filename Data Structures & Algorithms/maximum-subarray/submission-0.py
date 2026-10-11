class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, maxS = 0, min(nums)
        for num in nums:
            s += num
            maxS = max(maxS, s)

            if s < 0:
                s = 0
        
        return maxS