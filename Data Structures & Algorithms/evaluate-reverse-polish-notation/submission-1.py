class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '*', '-', '/'])
        st = deque()

        for token in tokens:
            if token not in operators:
                st.append(int(token))
            else:
                a, b = int(st.pop()), int(st.pop())

                res = None
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = b - a
                elif token == '*':
                    res = a * b
                else:
                    res = b / a
                
                st.append(int(res))

        return st[-1]