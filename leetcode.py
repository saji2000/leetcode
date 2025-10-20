class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in '+-/*':
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                if i == '+':
                    num = num1 + num2
                elif i == '-':
                    num = num1 - num2
                elif i == '/':
                    num = int(num1 / num2)
                else:
                    num = num1 * num2
                stack.append(num)
            else:
                stack.append(int(i))
        return stack.pop()