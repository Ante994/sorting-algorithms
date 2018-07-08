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
        last_parent = length // 2

        for i in range(last_parent, -1, -1):
            self.heap_order(lst, i, length)
        
        # sorting 
        for i in range(length, 0, -1):
            if lst[0] > lst[i]:
                lst[0], lst[i] = lst[i], lst[0]
                self.heap_order(lst, 0, i-1)

    def heap_order(self, lst, parent_position, lenght):
        child_position = 2*parent_position+1

        while child_position <= lenght:
            # if child exist and right child is > then left child
            if (child_position < lenght) and (lst[child_position+1] > lst[child_position]):
                child_position +=1
            
            # right child is > then parent
            if lst[child_position] > lst[parent_position]:
                lst[child_position], lst[parent_position] = lst[parent_position], lst[child_position]
                # move to the biggest child
                parent_position = child_position
                child_position = 2*parent_position+1
            else:
                return #force exit
