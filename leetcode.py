class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []


        def backtrack(start, substr):
            if start >= len(s):
                result.append(substr.copy())
            
            for end in range(start, len(s)):
                if s[start:end + 1] == s[start:end + 1][::-1]:
                    substr.append(s[start:end + 1])
                    backtrack(end + 1, substr)
                    substr.pop()
            
        backtrack(0, [])
        return result