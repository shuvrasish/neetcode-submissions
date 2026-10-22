class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not n:
                return 0
            
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[-1])
        
        def rob_range(start: int, end: int) -> int:
            n = end - start + 1

            if not n:
                return 0
            
            if n == 1:
                return nums[start]

            if n == 2:
                return max(nums[start], nums[end])
            
            dp = [0] * n
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])

            for i in range(2, n):
                dp[i] = max(nums[start + i] + dp[i - 2], dp[i - 1])
            
            return dp[n-1]
        
        return max(rob_range(0, n - 2), rob_range(1, n - 1))