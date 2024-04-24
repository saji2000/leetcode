class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif len(stack) > 0:
                pop = stack.pop()
                if i == ")" and pop != "(":
                    return False
                elif i == "}" and pop != "{":
                    return False
                elif i == "]" and pop != "[":
                    return False
            else:
                return False
        return len(stack) == 0