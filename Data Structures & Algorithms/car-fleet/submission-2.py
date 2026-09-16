class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        comb = []

        for i in range(n):
            comb.append((position[i], speed[i]))

        comb.sort(key=lambda x: x[0])

        st = []
        finishTime = [float('inf')] * n

        for i, (pos, sp) in enumerate(comb):
            distLeft = target - pos
            timeReq = distLeft / sp
            finishTime[i] = timeReq
        
        for i in range(n-1, -1, -1):
            if st:
                if finishTime[i] <= st[-1]:
                    continue
                else:
                    st.append(finishTime[i])
            else:
                st.append(finishTime[i])

        return len(st)
