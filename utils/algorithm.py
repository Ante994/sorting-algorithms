import random

class AlgorithmHelper:

    def __init__(self, num_elements):
        self.lst = [random.randint(1, num_elements) for num in range(0, num_elements)]

    def is_sorted(self):
        for i in range(1, len(self.lst)):
            if self.is_less(self.lst[i - 1], self.lst[i]):
                return False
        
        return True

    def swap_elements(self, index_1, index_2):
        self.lst[index_1], self.lst[index_2] = self.lst[index_2],self.lst[index_1]

    def is_less(self, index_1, index_2):
        if self.lst[index_1] < self.lst[index_2]:
            return True

    def is_greater(self, index_1, index_2):
        if self.lst[index_1] > self.lst[index_2]:
            return True

    def print_elements(self):
        print(self.lst) 
