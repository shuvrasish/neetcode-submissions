class MedianFinder:

    def __init__(self):
        self.small, self.large = [], [] #small will be max heap and large will be min heap
        # for median, pop from small and multiply by -1 and pop from large and add with lhs and / 2.0: if len(small) == len(large)
        # pop from small and multiply with -1

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        heapq.heappush(self.large, -heapq.heappop(self.small))

        while len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
        
        