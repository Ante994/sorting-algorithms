from utils.algorithm import AlgorithmHelper

'''
can be very efficient, because there are no comparison
sort elemnts according to individual characters
sort numbers from least significant digit to most significant digit

radix sort depends on onthere sort algorithm whose time complexity is O(n),
otherwise it does not achieve O(nk) in total, counting sort is most of time used,
who is also efficient if we know the range of input values in advance, 
and just counnting the occurrance of each object
then we konw the index if each object in sorted list by using the time of occurance

Time Complexity: Best O(kn) - Average O(kn) - Worst O(kn)
where k is the length (of digits) of the longest number and n is the size of the input array
Memory Complexity: Worst O(kn)
When to use it: algorithm is efficient if we already know range of target values
'''

class RadixSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)
        self.radix = 10

    def sort(self):
        max_length = False
        tmp = -1
        placement = 1

        while not max_length:
            max_length = True

            buckets = [list() for _ in range(self.radix)]

            for i in self.lst:
                tmp = i // placement
                buckets[tmp % self.radix].append(i)
                if max_length and tmp > 0:
                    max_length = False

            a = 0
            for b in range(self.radix):
                buck = buckets[b]
                for i in buck:
                    self.lst[a] = i
                    a += 1

            placement *= self.radix

        
