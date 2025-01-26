from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(Counter(s))
        print(Counter(t))
        if Counter(s) == Counter(t):
            return True
        return False
    
solution = Solution()

print(solution.isAnagram("abc", "bca"))