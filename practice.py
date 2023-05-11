class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if(len(arr) < 2):
            return False

        ascend = True

        for i in range(len(arr)-1):
            if(ascend and arr[i] < arr[i+1]):
                continue
            elif(not ascend and arr[i] > arr[i+1]):
                continue
            elif(ascend and arr[i] > arr[i+1] and i != 0):
                ascend = False
                continue
            else:
                return False
        
        return not ascend