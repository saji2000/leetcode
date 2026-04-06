class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(closing, opening, cur):
            if len(cur) == 2 * n:
                result.append(cur)
                return
            
            if opening < n:
                backtrack(closing, opening + 1, cur + "(")
            
            if closing < opening:
                backtrack(closing + 1, opening, cur + ")")
        
        backtrack(0, 0, "")
        return result
            
