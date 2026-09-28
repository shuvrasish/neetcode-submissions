class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceHeap = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(distanceHeap, (-distance, (x, y)))

            if len(distanceHeap) > k:
                heapq.heappop(distanceHeap)
        
        return [[x, y] for _, (x, y) in distanceHeap]