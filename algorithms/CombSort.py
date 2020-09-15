'''
Comb Sort
Time Complexity: O(N*log(N))
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class CombSort(Algorithm):
    def __init__(self):
        super().__init__("Comb Sort")

    def algorithm(self):
        n = len(self.array)
        gap = n
        swapped = True
        while swapped is True:
            gap = int(gap/1.3)
            if gap <= 1:
                swapped = False
                gap = 1
            for i in range(n-gap):
                if  self.array[i] > self.array[i+gap]:
                    self.array[i], self.array[i+gap] = self.array[i+gap], self.array[i]
                    swapped = True
                    #visualise the sorting
                    self.update(i, i+gap)
