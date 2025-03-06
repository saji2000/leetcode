class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == '+':
                    result = num1 + num2
                elif i == '-':
                    result = num1 - num2
                elif i == '*':
                    result = num1 * num2
                elif i == '/':
                    result = int(num1 / num2)
                stack.append(result)
        return stack.pop()