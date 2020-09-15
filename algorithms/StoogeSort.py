'''
Stooge Sort
Time Complexity: O(N^(log 3/log 1.5))
Space Complexity: O(N)
'''

from algorithms.Algorithm import Algorithm

class StoogeSort(Algorithm):
    def __init__(self):
        super().__init__("Stooge Sort")

    def algorithm(self, L = None, H = None):
        if L is None and H is None:
            L = 0
            H = len(self.array) - 1
        if (self.array[L] > self.array[H]):
            self.array[L], self.array[H] = self.array[H], self.array[L]
            #visualise the sorting
            self.update(L, H)
        if H-L >= 2:
            X = int((H-L+1)/3)
            self.algorithm(L, H-X)
            self.algorithm(L+X, H)
            self.algorithm(L, H-X)
