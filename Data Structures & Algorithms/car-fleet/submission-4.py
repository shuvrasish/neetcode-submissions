class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        comb = []

        for i in range(n):
            comb.append((position[i], speed[i]))

        comb.sort(key=lambda x: x[0])

        fleets = 0
        lastTime = -1
        
        for i in range(n-1, -1, -1):
            finishTime = (target - comb[i][0]) / comb[i][1]

            if (lastTime != -1 and finishTime > lastTime) or not lastTime != -1:
                fleets += 1
                lastTime = finishTime

        return fleets
