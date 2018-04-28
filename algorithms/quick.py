import random
from utils.algorithm import AlgorithmHelper

# Choose pivot(middle element, first, LAST, or RANDOM)
# Reorder the list so that all elements with values less than the pivot come 
# before the pivot, while all elements with values greater than the pivot come after it
# Then pivot is in its final position. This is called the partition operation.
# Recursively apply the above steps to the sub-list of elements with smaller values 
# and separately the sub-list of elements with greater values.

# Time Complexity: Best O(n log n) - Average O(n log n) - Worst O(n^2)
# Memory Complexity: Worst O(log n)
# When to use it: choosing the right pivot is crucial, not stable,
# with good implementation can be two times faster then merge or heap sort

class QuickSort(AlgorithmHelper):
        
    def __init__(self, numElements):
        super().__init__(numElements)

    def _partition(self,lst, first, last):       
        # pivot = random.randint(first, last) # to choose pivot random 
        # self.swapElements(pivot, last)

        for i in range(first, last):
            if self.isLess(i, last):
                self.swapElements(i, first)
                first += 1
        self.swapElements(first, last)
        return first

    def _sort(self, lst, first, last):
        if first < last:
            pi = self._partition(lst,first,last)
            self._sort(lst, first, pi-1)
            self._sort(lst, pi+1, last)

    def sort(self):
        self._sort(self.lst, 0, len(self.lst) - 1)
