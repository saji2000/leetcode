class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif not stack:
                return False
            else:
                if stack.pop() != brackets[i]:
                    return False
        return not stack