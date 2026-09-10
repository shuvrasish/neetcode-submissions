class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = defaultdict(int)
        for c in s:
            dct[c] += 1
        
        for c in t:
            if c not in dct:
                return False
            else:
                dct[c] -= 1
                if dct[c] == 0:
                    del dct[c]
        
        if not dct:
            return True
        return False