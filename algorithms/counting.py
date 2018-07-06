from utils.algorithm import AlgorithmHelper

'''
Finds maximum element in the list of elements.
Initialize counter list with 0 for all elements range from 0 to maximum element.
Finds frequency for all array elements and updates frequency value in counter list.
Sorted array elements based on counter list.

Creats a bucket for each value
Maximum value in the input array must be know for creating buckets

Time Complexity: Best O(k+n) - Average O(k+n) - Worst O(k+n)
where n is the size of the input array and k means the values range from 0 to k.
Memory Complexity: Worst O(k + n)
When to use it: algorithm is efficient if we already know range of target values
'''

class CountingSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)
        self.k = len(self.lst)

    def sort(self):
        counter = [0] * (self.k+1)

        for i in self.lst:
            counter[i] += 1
    
        index = 0
        for i in range(len(counter)):
            while 0 < counter[i]:
                self.lst[index] = i
                index += 1
                counter[i] -= 1


