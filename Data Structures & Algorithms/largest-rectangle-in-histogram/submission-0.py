class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # formula: area = (i_nse - i_pse - 1) * heights[i]
        n = len(heights)
        if not n:
            return 0

        maxArea = 0
        st = []

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                # pop any element larger than it and it and check area for it
                # update max area var 

                popped = heights[st.pop()]

                nse = i
                pse = st[-1] if st else -1

                maxArea = max(maxArea, (nse - pse - 1) * popped)
            st.append(i)
        
        while st:
            # pop any element larger than it and it and check area for it
            # update max area var 

            popped = heights[st.pop()]

            nse = n
            pse = st[-1] if st else -1

            maxArea = max(maxArea, (nse - pse - 1) * popped)
        
        return maxArea