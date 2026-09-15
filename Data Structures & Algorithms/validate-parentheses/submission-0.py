class Solution:
    def isValid(self, s: str) -> bool:
        opposites = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = deque()

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if stack and stack[-1] == opposites[c]:
                    stack.pop()
                else:
                    return False
        
        return not stack
