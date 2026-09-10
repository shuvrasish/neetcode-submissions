class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res