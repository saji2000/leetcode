class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if(not (len(str(i)) % 2)):
                ans += 1
        
        return ans