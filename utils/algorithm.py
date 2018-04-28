
import random

class AlgorithmHelper:

    def __init__(self, numElements):
        self.lst = [random.randint(1, numElements) for num in range(0, numElements)]

    def isSorted(self):
        for i in range(1, len(self.lst)):
            if self.isLess(self.lst[i - 1], self.lst[i]):
                return False
        
        return True

    def swapElements(self, index1, index2):
        self.lst[index1], self.lst[index2] = self.lst[index2],self.lst[index1]

    def isLess(self, index1, index2):
        if self.lst[index1] < self.lst[index2]:
            return True

    def isGretter(self, index1, index2):
        if self.lst[index1] > self.lst[index2]:
            return True

    def printElements(self):
        print(self.lst) 
