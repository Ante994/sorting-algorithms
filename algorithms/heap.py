from utils.algorithm import AlgorithmHelper

'''
 Heap sort happens in two phases. In the first phase, the array
 is transformed into a heap (func. HEAP OREDER). A heap is a binary tree where
 1) each node is greater than each of its children
 2) the tree is perfectly balanced
 3) all leaves are in the leftmost position available
 In phase two the heap is continuously reduced to a sorted array:
 1) while the heap is not empty
 - remove the top of the head into an array
 - fix the heap

Heap Order (heap structure):
checks that an element is greater than its children, if not the values of element
and child are swapped. The function continues to check and swap until the element is at a
position where it is greater than its children.

Time Complexity: Best O(nlog(n)) - Average O(nlog(n)) - Worst O(nlog(n)).
where k is the length (of digits) of the longest number and n is the size of the input array
Memory Complexity: Worst O(1)
When to use it: in embedded systems where less space is available, n
'''

class HeapSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)

    def sort(self):
        self._sort(self.lst)

    def _sort(self, lst):
        # making heap, P >= C (parent, child)
        length = len(lst) - 1
        parent = length // 2

        for i in range(parent, -1, -1):
            self.heap_order(lst, i, length)
        
        # sorting 
        for i in range(length, 0, -1):
            if lst[0] > lst[i]:
                lst[0], lst[i] = lst[i], lst[0]
                self.heap_order(lst, 0, i-1)


    def heap_order(self, lst, first, last):
        largest = 2*first+1

        while largest <= last:
            # if child exist and child is > then left child
            if (largest < last) and (lst[largest] < lst[largest+1]):
                largest +=1
            
            # right child is > then parent
            if lst[largest] > lst[first]:
                lst[largest], lst[first] = lst[first], lst[largest]
                # move to the biggest child
                first = largest
                largest = 2*first+1
            else:
                return #force exit