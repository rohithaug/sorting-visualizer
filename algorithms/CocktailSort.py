'''
Cocktail shaker sort (also known as bidirectional bubble sort, cocktail sort, shaker sort, ripple sort, shuffle sort, or shuttle sort)
Time Complexity: O(N*N)
Space Complexity: 1
'''

from algorithms.Algorithm import Algorithm

class CocktailSort(Algorithm):
    def __init__(self):
        super().__init__("Cocktail Sort")

    def algorithm(self):
        swapped = True
        start = 0
        end = len(self.array)-1
        while swapped:
            swapped = False
            for i in range(start, end):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    #visualise the sorting
                    self.update(i, i+1)
                    swapped = True
            if swapped is False:
                break
            swapped = False
            end -= 1
            for i in range(end, start, -1):
                if self.array[i] < self.array[i-1]:
                    self.array[i], self.array[i-1] = self.array[i-1], self.array[i]
                    #visualise the sorting
                    self.update(i-1, i)
                    swapped = True
            start += 1
