class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in reversed(range(len(arr))):

            temp = arr[i]
            arr[i] = greatest
            greatest = max(greatest, temp)
            
        return arr