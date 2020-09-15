'''
Heap Sort
Time Complexity: O(N*log(N))
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("Heap Sort")

    def algorithm(self):
        n = len(self.array)//2 - 1
        #Build a Max Heap
        for i in range(n, -1, -1):
            self.heapify(len(self.array), i)
        #Sort the elements
        for i in range(len(self.array)-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            #visualise the sorting
            self.update(i)
            self.heapify(i, 0)

    def heapify(self, size, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < size and self.array[left] > self.array[largest]:
            largest = left

        if right < size and self.array[right] > self.array[largest]:
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            #visualise the sorting
            self.update(i, largest)
            self.heapify(size, largest)
