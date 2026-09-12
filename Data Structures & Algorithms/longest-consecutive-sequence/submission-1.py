class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        s = set()

        for num in nums:
            s.add(num)

        lcs = 1

        for num in nums:
            if num - 1 not in s:
                x = num
                mxl = 0
                while x in s:
                    x = x + 1
                    mxl += 1
                
                lcs = max(lcs, mxl)
        
        return lcs