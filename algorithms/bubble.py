import random
from utils.algorithm import AlgorithmHelper

'''
Repeatedly stepping through the list to be sorted
Comparing each pair of elemnts and swapping them 
if they are in the wrong order

Time Complexity: Best O(n) - Average O(n^2) - Worst O(n^2)
Memory Complexity: Worst O(1)
When to use it: only when all elements are almost sorted
'''

class BubbleSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)

    def sort(self):
        for i in range(len(self.lst)):
            self.swapped = False
            for j in range(0, len(self.lst) - i-1):
                if self.is_greater(j, j+1):
                    self.swap_elements(j, j+1)
                    self.swapped = True

            if self.swapped == False:
                break