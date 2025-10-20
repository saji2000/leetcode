class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                opening = stack.pop()
                if i == ')' and opening != '(':
                    return False
                elif i == '}' and opening != '{':
                    return False
                elif i == ']' and opening != '[':
                    return False
        return len(stack) == 0