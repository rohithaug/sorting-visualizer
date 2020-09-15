'''
Shell Sort
Time Complexity: Depends on gap sequence. Here it is O(N*N) since N = 512 = 2^9
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class ShellSort(Algorithm):
    def __init__(self):
        super().__init__("Shell Sort")

    def algorithm(self):
        n = len(self.array)
        gap = n//2
        while gap > 0:
            for i in range(gap, n):
                temp = i
                j = temp - gap
                while j >= 0 and self.array[temp] < self.array[j]:
                    self.array[temp], self.array[j] = self.array[j], self.array[temp]
                    #visualise the sorting
                    self.update(temp, j)
                    temp -= gap
                    j -= gap
            gap //= 2
