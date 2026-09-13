class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = defaultdict(int)
        maxl = 1
        l, r = 0, 0
        while l <= r and r < len(s):
            # print(f"d: {d}, pos: l={l}, r={r}")
            d[s[r]] += 1

            while d[s[r]] > 1 and l <= r:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            
            maxl = max(maxl, len(d))
            r += 1
        
        return maxl


