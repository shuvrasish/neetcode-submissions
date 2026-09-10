class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded = encoded + (str(len(s)) + "#" + s)
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length_of_word = int(s[i:j])

            j += 1

            word = s[j:j + length_of_word]

            res.append(word)

            i = j + length_of_word

        return res
