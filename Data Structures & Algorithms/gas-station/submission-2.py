class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        starting = 0
        total = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            if total < 0:
                total = 0
                starting = i + 1
        
        return starting