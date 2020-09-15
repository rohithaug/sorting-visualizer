'''
Insertion Sort
Time Complexity: O(N*N)
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("Insertion Sort")

    def algorithm(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j = j-1
            self.array[j+1] = key
            #visualise the sorting
            self.update(j+1)
