class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        totalArea = 0
        maxl = height[l]
        maxr = height[r]

        while l < r:
            if height[l] < height[r]:
                if maxl > height[l]:
                    totalArea += maxl - height[l]
                else:
                    maxl = height[l]
                l += 1
            else:
                if maxr > height[r]:
                    totalArea += maxr - height[r]
                else:
                    maxr = height[r]
                r -= 1
        
        return totalArea
                    
                

