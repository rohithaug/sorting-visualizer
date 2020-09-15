'''
Bubble Sort
Time Complexity: O(N*N)
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("Bubble Sort")

    def algorithm(self):
        swap = False
        for i in range(len(self.array)-1):
            for j in range(len(self.array)-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    swap = True
                    #visualise the sorting
                    self.update(j, j+1)
            if swap == False:
                break
