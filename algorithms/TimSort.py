'''
Tim Sort
Time Complexity: O(N*log(N))
Space Complexity: O(N)
'''

from algorithms.Algorithm import Algorithm

class TimSort(Algorithm):
    def __init__(self):
        super().__init__("Tim Sort")

    def algorithm(self):
        RUN = 32
        n = len(self.array)
        for i in range(0, n, RUN):
            self.InsertionSort(i, min(i+32, n))
        size = RUN
        while size < n:
            for left in range(0, n, 2*size):
                mid = left + size
                right = min(mid+size, n)
                self.Merge(left, mid, right)
            size *= 2

    def InsertionSort(self, left, right):
        for i in range(left, right):
            key = self.array[i]
            j = i-1
            while j >= left and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j = j-1
            self.array[j+1] = key
            #visualise the sorting
            self.update(j+1)

    def Merge(self, l, m, r):
        left = self.array[l:m]
        right = self.array[m:r]

        #i - index of left array, j - index of right array, k - index of self.array
        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1
            #visualise the sorting
            self.update(k)
            k += 1

        while i < len(left):
            self.array[k] = left[i]
            #visualise the sorting
            self.update(k)
            i += 1
            k += 1

        while j < len(right):
            self.array[k] = right[j]
            #visualise the sorting
            self.update(k)
            j += 1
            k += 1
