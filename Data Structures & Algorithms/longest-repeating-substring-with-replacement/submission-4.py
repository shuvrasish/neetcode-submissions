class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        d = defaultdict(int)
        maxf = 0

        ans = 0

        while l <= r and r < n:
            d[s[r]] += 1
            maxf = max(maxf, d[s[r]])

            changes = (r - l + 1) - maxf
            if changes > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            else:
                ans = max(ans, r - l + 1)

            r += 1
                
        return ans


