import random
from utils.algorithm import AlgorithmHelper

'''
Find the smallest element then swap it with the element at index i (i = 0)
Find the second smallest element then swap it with the element at index i + 1
Repeat until all elements are sorted

Time Complexity: Best O(n^2) - Average O(n^2) - Worst O(n^2)
Memory Complexity: Worst O(1)
When to use it: When the cost of a swap is large (long string), for small number of elements
'''

class SelectionSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)

    def sort(self):
        key = 0

        for i in range(len(self.lst)):
            key = i        
            for j in range(i, len(self.lst)):
                if self.is_less(j, key):
                    key = j
            self.swap_elements(i, key)
