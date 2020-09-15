'''
Selection Sort
Time Complexity: O(N*N)
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("Selection Sort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            #visualise the sorting
            self.update(i, min_index)
