class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minEls = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minEls[-1] if self.minEls else val)
        self.minEls.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minEls.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minEls[-1]
