class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not n:
            return 0

        if n <= 2:
            return max(nums[0], nums[n - 1])
        
        dpf = [0] * n
        dpl = [0] * n

        dpf[0] = nums[0]
        dpf[1] = max(nums[0], nums[1])

        dpl[0] = 0
        dpl[1] = nums[1]

        for i in range(2, n - 1):
            dpf[i] = max(nums[i] + dpf[i - 2], dpf[i - 1])
        
        for i in range(2, n):
            dpl[i] = max(nums[i] + dpl[i - 2], dpl[i - 1])
        
        return max(dpl[n - 1], dpf[n - 2])