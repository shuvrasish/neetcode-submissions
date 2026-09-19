class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(dict)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].update({
            timestamp: value
        })
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        if timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
        maxTimeStamp = float('-inf')
        for prev_timestamp, status in self.timeMap[key].items():
            if prev_timestamp < timestamp and prev_timestamp >= maxTimeStamp:
                maxTimeStamp = prev_timestamp
        
        return self.timeMap[key][maxTimeStamp] if maxTimeStamp != float('-inf') else ""

        
