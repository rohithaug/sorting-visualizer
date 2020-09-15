'''
Gnome Sort (dubbed Stupid Sort)
Time Complexity: O(N*N)
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class GnomeSort(Algorithm):
    def __init__(self):
        super().__init__("Gnome Sort")

    def algorithm(self):
        i = 0
        while i < len(self.array):
            if i == 0 or self.array[i] >= self.array[i-1]:
                i += 1
            else:
                self.array[i], self.array[i-1] = self.array[i-1], self.array[i]
                #visualise the sorting
                self.update(i-1)
                i -= 1
