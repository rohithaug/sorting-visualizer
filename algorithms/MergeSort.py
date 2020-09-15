'''
Merge Sort
Time Complexity: O(N*log(N))
Space Complexity: N
'''

from algorithms.Algorithm import Algorithm

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("Merge Sort")

    def algorithm(self, temp_array = [], index = 0):
        if temp_array == []:
            temp_array = self.array.copy()

        if len(temp_array) > 1:
            m = len(temp_array)//2
            left = temp_array[:m]
            right = temp_array[m:]

            self.algorithm(left, index)
            self.algorithm(right, index+m)

            #i - index of left array, j - index of right array, k - index of temp merged array
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    if self.array[index] != left[i]:
                        self.array[index], self.array[index-j+m] = left[i], self.array[index]
                        self.update(index, index-j+m)
                    else:
                        self.array[index] = left[i]
                        self.update(index)
                    temp_array[k] = left[i]
                    i += 1
                else:
                    self.array[index], self.array[index-i+m] = right[j], self.array[index]
                    self.update(index, index-i+m)
                    temp_array[k] = right[j]
                    j += 1
                #visualise the sortingm+k
                index += 1
                k += 1

            while i < len(left):
                self.array[index] = left[i]
                temp_array[k] = left[i]
                #visualise the sorting
                self.update(index)
                index += 1
                i += 1
                k += 1

            while j < len(right):
                self.array[index] = right[j]
                temp_array[k] = right[j]
                #visualise the sorting
                self.update(index)
                index += 1
                j += 1
                k += 1
