class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = dict()

        for i in range(len(nums)):
            if target - nums[i] in myDict:
                return [i, myDict[target - nums[i]]]
            myDict[nums[i]] = i
        return