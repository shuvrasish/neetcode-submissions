class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        timestampValuePairs = self.timeMap[key]

        l, r = 0, len(timestampValuePairs) - 1
        ans = ""
        while l <= r:
            mid = l + (r - l) // 2

            if timestampValuePairs[mid][0] > timestamp:
                r = mid - 1
            else:
                ans = timestampValuePairs[mid][1]
                l = mid + 1
        
        return ans

        
