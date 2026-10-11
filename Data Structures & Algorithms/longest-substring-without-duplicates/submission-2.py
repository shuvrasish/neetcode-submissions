class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        d = defaultdict(int)

        l, r = 0, 0
        maxl = 1
        while l <= r and r < len(s):
            d[s[r]] += 1

            while d[s[r]] > 1 and l <= r:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            
            maxl = max(maxl, len(d))
            r += 1
            
        
        return maxl

