class Solution:
    def calcHours(self, piles: List[int], speed: int) -> int:
        totalHrs = 0
        for numBananas in piles:
            totalHrs += math.ceil(numBananas / speed)
        
        return totalHrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min speed = 0 -> if speed is less than this, koko will never finish eating bananas
        #max speed = max(piles) -> if this is the speed, koko finishes in len(piles) days

        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = l + (r - l) // 2

            numHrsReq = self.calcHours(piles, mid)

            if numHrsReq > h:
                l = mid + 1
            else:
                ans = min(ans, mid)
                r = mid - 1
        
        return ans

        