'''
Radix Sort                      ; Sort from Least Significant Digit to Most Significant Digit
Time Complexity: O(w*N)         ; m is the number of bits required to store each element
Space Complexity: O(w+N)
'''

from algorithms.Algorithm import Algorithm

class RadixSort(Algorithm):
    def __init__(self):
        super().__init__("Radix Sort")

    def algorithm(self):
        maximum = max(self.array)
        #Applying Counting Sort to sort elements based on place from LSD to MSD
        place = 1
        while maximum//place > 1:
            self.PlacesCountingSort(place)
            place *= 10

    def PlacesCountingSort(self, place):
        count = [0] * (10)
        for i in self.array:
            count[(i//place)%10] += 1
        for i in range(1, 10):
            count[i] = count[i] + count[i-1]
        temp = self.array.copy()
        for i in reversed(temp):
            index = (i//place)%10
            self.array[count[index]-1] = i
            #visualise the sorting
            self.update(count[index]-1)
            count[index] -= 1
