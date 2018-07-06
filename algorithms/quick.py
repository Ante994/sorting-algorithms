import random
from utils.algorithm import AlgorithmHelper

'''
Choose pivot(middle element, first, LAST, or RANDOM)
Reorder the list so that all elements with values less than the pivot come 
before the pivot, while all elements with values greater than the pivot come after it
Then pivot is in its final position. This is called the partition operation.
Recursively apply the above steps to the sub-list of elements with smaller values 
and separately the sub-list of elements with greater values.

Time Complexity: Best O(n log n) - Average O(n log n) - Worst O(n^2)
Memory Complexity: Worst O(log n)
When to use it: choosing the right pivot is crucial, not stable,
# with good implementation can be two times faster then merge or heap sort
'''

import random

class QuickSortBasic(AlgorithmHelper):
    def __init__(self, numElements):
        super().__init__(numElements)

    def _sort(self, lst):
        if len(lst) < 1:
            return lst

        smaller, equal, bigger = [], [], []
        pivot = lst[random.randint(0, len(lst)-1)]

        for x in lst:
            if x < pivot:
                smaller.append(x)
            elif x > pivot:
                bigger.append(x)
            else:
                equal.append(x)

        return self._sort(smaller) + equal + self._sort(bigger)


    def sort(self):
        self.lst = self._sort(self.lst)


class QuickSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)

    def _partition(self,lst, first, last):       
        pivot = random.randint(first, last) # to choose pivot random 
        self.lst[pivot], self.lst[last] = self.lst[last], self.lst[pivot]

        # lines that are commented - cost too much time !!! better without OOP
        for i in range(first, last):
            #if self.is_less(i, last):
            if self.lst[i] <= self.lst[last]:
                #self.swap_elements(i, first)
                self.lst[i], self.lst[first] = self.lst[first], self.lst[i]
                first += 1
        #self.swap_elements(first, last)
        self.lst[first], self.lst[last] = self.lst[last], self.lst[first]
        return first

    def _sort(self, lst, first, last):
        if first < last:
            pi = self._partition(lst,first,last)
            self._sort(lst, first, pi-1)
            self._sort(lst, pi+1, last)

    def sort(self):
        self._sort(self.lst, 0, len(self.lst) - 1)