'''
Pancake Sort
Time Complexity: O(N*N)
Space Complexity: O(N)
'''

from algorithms.Algorithm import Algorithm

class PancakeSort(Algorithm):
    def __init__(self):
        super().__init__("Pancake Sort")

    def algorithm(self):
        size = len(self.array)
        while size > 1:
            max_index = self.findMax(size)
            #visualise the sorting
            self.update(None, None, max_index)
            if max_index != size-1:
                self.flip(max_index)
                #visualise the sorting
                self.update(0)
                self.flip(size-1)
                #visualise the sorting
                self.update(size-1)
            size -= 1

    def findMax(self, n):
        max = 0
        for i in range(1, n):
            if self.array[i] > self.array[max]:
                max = i
        return max

    def flip(self, n):
        start = 0
        while start < n:
            self.array[start], self.array[n] = self.array[n], self.array[start]
            start += 1
            n -= 1
