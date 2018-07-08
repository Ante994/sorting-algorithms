from utils.algorithm import AlgorithmHelper

'''
divide and conquer, comparison based, stable
not in place, require additional memory, but for linked list its only O(1)
good implementation of quicksort outperform mergsort
Divide into 2 collections. Mergesort will take the middle index in the collection and split it into the left and right parts based on this middle index.
Resulting collections are again recursively splited and sorted
Once the sorting of the two collections is finished, the results are merged
Now Mergesort it picks the item which is smaller and inserts this item into the new collection.
Then selects the next elements and sorts the smaller element from both collections

Time Complexity: Best O(n log n) - Average O(n log n) - Worst O(n log n )
Memory Complexity: Worst O(n)
When to use it: 
'''

class MergeSort(AlgorithmHelper):
        
    def __init__(self, num_elements):
        super().__init__(num_elements)

    def _sort(self, lst, left, mid, right):
        n1 = mid-left+1
        n2 = right - mid
    
        # temp lst for L and R
        LEFT = [0] * (n1)
        RIGHT = [0] * (n2)
    
        # copy elem. to LEFT[] and RIGHT[]
        for i in range(0 , n1):
            LEFT[i] = lst[left + i]
    
        for j in range(0 , n2):
            RIGHT[j] = lst[mid + 1 + j]
    
        # Merge the temp lstays back into lst[left..right]
        i = 0     # Initial index of first sublstay
        j = 0     # Initial index of second sublstay
        k = left     # Initial index of merged sublstay
    
        while i < n1 and j < n2 :
            if LEFT[i] <= RIGHT[j]:
                lst[k] = LEFT[i]
                i += 1
            else:
                lst[k] = RIGHT[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of LEFT[], if there are any
        while i < n1:
            lst[k] = LEFT[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of RIGHT[], if there are any
        while j < n2:
            lst[k] = RIGHT[j]
            j += 1
            k += 1

    def sort(self):
        self.mergesort(self.lst, 0, len(self.lst) - 1)
    
    def mergesort(self, lst, left, right):
        if left < right:
            mid = (left+(right-1)) // 2
 
            self.mergesort(lst, left, mid)
            self.mergesort(lst, mid+1, right)
            self._sort(lst, left, mid, right)