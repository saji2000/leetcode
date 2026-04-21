class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        nums = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(i, cur):
            if len(cur) == len(digits):
                result.append(cur[:])
                return
            
            for letter in nums[digits[i]]:
                backtrack(i + 1, cur + letter)
        
        backtrack(0, "")
        return result