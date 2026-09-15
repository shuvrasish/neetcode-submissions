class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]

        st = deque()
        res = [0] * n
        st.append(n-1)

        for i in range(n - 2, -1, -1):
            temp = temperatures[i]

            while st and temperatures[st[-1]] <= temp:
                st.pop()
            
            res[i] = (st[-1] - i) if st else 0
            st.append(i)
        
        return res