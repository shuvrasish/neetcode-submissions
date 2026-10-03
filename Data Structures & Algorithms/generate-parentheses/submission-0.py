class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def dfs(openc: int, closedc: int) -> None:
            if openc == closedc and closedc == n:
                res.append("".join(sub[:]))
                return
            
            if openc < n:
                # add another open
                sub.append("(")
                dfs(openc + 1, closedc)
                sub.pop()

            # close one
            if openc > closedc:
                sub.append(")")
                dfs(openc, closedc + 1)
                sub.pop()

        dfs(0, 0)
        return res