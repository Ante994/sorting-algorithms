import random
from utils.algorithm import AlgorithmHelper


# Iterates through the elements, taking one element at each repetition
# Removes one element, finds the location where it belongs and inserts it there
# Repeats until no input elements remain.

# Time Complexity: Best O(n) - Average O(n^2) - Worst O(n^2)
# Memory Complexity: Worst O(1)
# When to use it: for small number of elements, when elements are almost sorted

class InsertionSort(AlgorithmHelper):
        
    def __init__(self, numElements):
        super().__init__(numElements)

    def sort(self):
        for i in range(1, len(self.lst)):
            for j in range(i, 0, -1):
                if self.isLess(j, j - 1):
                    self.swapElements(j, j - 1)
