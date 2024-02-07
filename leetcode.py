class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        return False