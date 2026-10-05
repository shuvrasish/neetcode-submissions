class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        numberToChar = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        parsedInput = [int(digit) for digit in digits]

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


        