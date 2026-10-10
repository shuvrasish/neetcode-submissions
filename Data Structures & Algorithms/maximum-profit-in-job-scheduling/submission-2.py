class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(start, end, jobProfit) for start, end, jobProfit in zip(startTime, endTime, profit)]
        jobs.sort()
        n = len(jobs)

        cache = {}

        def dfs(i: int) -> int:
            if i >= n:
                return 0

            if i in cache:
                return cache[i]
            
            res = dfs(i + 1)
            take = jobs[i][2]

            l, r = i, n - 1
            nextAvailable = -1

            while l <= r:
                mid = l + (r - l) // 2

                if jobs[mid][0] < jobs[i][1]:
                    l = mid + 1
                else:
                    nextAvailable = mid
                    r = mid - 1
    
            if nextAvailable != -1:
                take += dfs(nextAvailable)
            
            cache[i] = res = max(res, take)
            
            return res
        
        return dfs(0)