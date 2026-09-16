class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        comb = []

        for i in range(n):
            comb.append((position[i], speed[i]))

        comb.sort(key=lambda x: x[0])

        st = []
        
        for i in range(n-1, -1, -1):
            finishTime = (target - comb[i][0]) / comb[i][1]

            if (st and finishTime > st[-1]) or not st:
                st.append(finishTime)

        return len(st)
