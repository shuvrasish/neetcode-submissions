class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        if n < len(t):
            return ""

        hs = defaultdict(int)

        for c in t:
            hs[c] += 1
        
        l, r = 0, 0
        minlen = float('inf')
        toFind = len(hs)
        startIndex = -1

        while l <= r and r < n:
            hs[s[r]] -= 1
            if hs[s[r]] == 0:
                toFind -= 1
            
            while not toFind:
                if r - l + 1 < minlen:
                    startIndex = l
                    minlen = r - l + 1
                hs[s[l]] += 1
                if hs[s[l]] > 0:
                    toFind += 1
                l += 1
            
            r += 1
        
        return s[startIndex: startIndex + minlen] if startIndex != -1 else ""
                
                    


