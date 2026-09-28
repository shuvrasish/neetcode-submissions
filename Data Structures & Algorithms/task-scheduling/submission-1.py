class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []

        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1
        
        for frequency in freq.values():
            heapq.heappush(heap, -frequency)
        
        time = 0
        q = deque() # pair [-cnt, available_at time]

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1 # executing the task

                if cnt != 0:
                    q.append((cnt, n + time))

            if q and q[0][1] == time:
                heapq.heappush(heap, q[0][0])
                q.popleft()
        
        return time
