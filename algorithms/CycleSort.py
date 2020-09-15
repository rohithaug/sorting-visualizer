'''
Cycle Sort
Time Complexity: O(N*N)
Space Complexity: O(1)
'''

from algorithms.Algorithm import Algorithm

class CycleSort(Algorithm):
    def __init__(self):
        super().__init__("Cycle Sort")

    def algorithm(self):
        n = len(self.array)
        for cycleStart in range(n-1):
            item = self.array[cycleStart]
            pos = cycleStart
            for i in range(cycleStart+1, n):
                if self.array[i] < item:
                    pos += 1
            if pos == cycleStart:
                continue
            while self.array[pos] == item:
                pos += 1
            self.array[pos], item = item, self.array[pos]
            #visualise the sorting
            self.update(pos, cycleStart, cycleStart)
            while pos != cycleStart:
                swap = pos
                pos = cycleStart
                for i in range(cycleStart+1, n):
                    if self.array[i] < item:
                        pos += 1
                while self.array[pos] == item:
                    pos += 1
                self.array[pos], item = item, self.array[pos]
                #visualise the sorting
                self.update(pos, swap, cycleStart)
