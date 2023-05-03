class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        consecutive = 0
        for i in nums:
            if(i == 1):
                consecutive += 1
            else:
                consecutive = 0
            if(consecutive > ans):
                ans = consecutive
        return ans