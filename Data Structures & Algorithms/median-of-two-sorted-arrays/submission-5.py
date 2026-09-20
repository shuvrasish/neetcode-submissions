class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (m + n + 1) // 2

        l, r = 0, m

        while l <= r:
            mid = l + (r - l) // 2

            l1 = mid
            l2 = k - l1
            
            a = nums1[l1 - 1] if l1 > 0 else float('-inf')
            b = nums2[l2 - 1] if l2 > 0 else float('-inf')
            c = nums1[l1] if l1 < m else float('inf')
            d = nums2[l2] if l2 < n else float('inf')

            if a > d:
                r = mid - 1
            elif b > c:
                l = mid + 1
            else:
                totalLen = m + n
                if totalLen % 2 == 0:
                    return (max(a,b) + min(c,d)) / 2 
                return max(a,b)

        return -1