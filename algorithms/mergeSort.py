# Merge Sort algorithm
class Sort:
    def mergeSort(self, arr):
        n = len(arr)

        if n > 1:
            left_arr = arr[:n//2]
            right_arr = arr[n//2:]

            self.mergeSort(left_arr)
            self.mergeSort(right_arr)

            i = 0
            j = 0
            k = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] > right_arr[j]:
                    arr[k] = right_arr[j]
                    j += 1
                else:
                    arr[k] = left_arr[i]
                    i += 1
                k += 1
            
            if k < n:
                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
        return arr


sort = Sort()

print(sort.mergeSort([1, 6, 7, 3, 9, 0, 2]))
