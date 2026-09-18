class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        ans = float('inf')
        while l <= r:
            mid = l + (r - l) // 2

            #left half sorted? take min and eliminate left
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            #right half sorted? take min and eliminate right
            else:
                ans = min(ans, nums[mid])
                r = mid - 1

        return ans