class Sort:
    def mergeSort(self, arr):
        n = len(arr)
        if n > 1:
            left = arr[:n//2]
            right = arr[n//2:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    arr[k] = right[j]
                    j += 1
                else:
                    arr[k] = left[i]
                    i += 1
                k += 1

            # Add remaining elements from left
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            # Add remaining elements from right
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                
        return arr


sort = Sort()

print(sort.mergeSort([1, 6, 7, 3, 9, 0, 2]))
