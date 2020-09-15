'''
Bitonic Sort                                ; Size of input should be of the form 2^p
Time Complexity: O(log^2(N))                ; log^2(N) = log(log(N))
Space Complexity: O(N * log^2(N))
'''

import sys
from algorithms.Algorithm import Algorithm

class BitonicSort(Algorithm):
    def __init__(self):
        super().__init__("Bitonic Sort")

    def algorithm(self, low = 0, count = None, ASC = True):
        if not self.checkIsPowerOfTwo():
            sys.exit("Error: Size of input array is not of the form 2^p")
        if count == None:
            count = len(self.array)
        if count > 1:
            self.algorithm(low, count//2, True)
            self.algorithm(low + count//2, count//2, False)
            self.BitonicMerge(low, count, ASC)

    def BitonicMerge(self, low, count, ASC):
        if count > 1:
            self.BitonicCompare(low, count, ASC)
            self.BitonicMerge(low, count//2, ASC)
            self.BitonicMerge(low + count//2, count//2, ASC)

    def BitonicCompare(self, low, count, ASC):
        m = count//2
        for i in range(low, low+m):
            if (self.array[i] > self.array[m+i]) is ASC:
                self.array[i], self.array[m+i] = self.array[m+i], self.array[i]
                #visualise the sorting
                self.update(i, m+i)

    def checkIsPowerOfTwo(self):
        n = len(self.array)
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True
