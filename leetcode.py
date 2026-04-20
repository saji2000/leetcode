class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        nums = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i, comb):
            if len(comb) == len(digits):
                result.append(comb[:])
                return
            
            for letter in nums[digits[i]]:
                print(i)
                print(comb + letter)
                backtrack(i + 1, comb + letter)
        
        backtrack(0, "")
        return result

solution = Solution()
print(solution.letterCombinations("234"))