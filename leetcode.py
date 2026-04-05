class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(opening, closing, cur):
            if len(cur) == 2 * n:
                result.append(cur)
                return
            if opening < n:
                backtrack(opening + 1, closing, cur + '(')
                
            if closing < opening:
                backtrack(opening, closing + 1, cur + ')')
        
        backtrack(0, 0, "")
        return result