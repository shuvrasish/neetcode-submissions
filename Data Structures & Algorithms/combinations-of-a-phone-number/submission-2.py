class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        numberToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        parsedInput = [digit for digit in digits]

        res = []
        sub = []
        def dfs(i: int) -> None:
            if i == len(parsedInput):
                res.append("".join(sub))
                return

            digit = parsedInput[i]
            
            for char in numberToChar[digit]:
                sub.append(char)
                dfs(i + 1)
                sub.pop()
        
        dfs(0)
        return res


        