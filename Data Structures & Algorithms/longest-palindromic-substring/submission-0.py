class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)

        startIndex = 0
        maxLen = 1
        for i in range(n):
            #odd
            l, r = i, i

            sLen = 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    startIndex = l
                    maxLen = r - l + 1
                l -= 1
                r += 1

            #even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    startIndex = l
                    maxLen = r - l + 1
                l -= 1
                r += 1
        
        return s[startIndex: startIndex + maxLen]