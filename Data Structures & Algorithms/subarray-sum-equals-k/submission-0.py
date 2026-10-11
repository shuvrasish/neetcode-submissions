class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hs = {0: 1}

        count = 0
        for num in nums:
            prefixSum += num

            if prefixSum - k in hs:
                count += hs[prefixSum - k]
            
            if prefixSum in hs:
                hs[prefixSum] += 1
            else:
                hs[prefixSum] = 1

        return count
        
