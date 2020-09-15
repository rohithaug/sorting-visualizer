'''
Quick Sort
Time Complexity: O(N*log(N))
Space Complexity: O(log(N))
'''

from algorithms.Algorithm import Algorithm

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("Quick Sort")

    def algorithm(self, low = None, high = None):
        if low is None and high is None:
            low = 0
            high = len(self.array)
        if low < high:
            pivot = self.partition(low, high)
            self.algorithm(low, pivot)
            self.algorithm(pivot+1, high)

    def partition(self, low, high):
        #pivot element is the smallest element in the array
        pivot = self.array[low]
        j = low
        for i in range(low+1, high):
            if self.array[i] < pivot:
                j += 1
                self.array[j], self.array[i] = self.array[i], self.array[j]
                #visualise the sorting
                self.update(j, i, low)
        self.array[j], self.array[low] = self.array[low], self.array[j]
        #visualise the sorting
        self.update(j, low)
        return j
