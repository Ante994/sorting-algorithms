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

    def _sort(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    
        # Copy data to temp arrays L[] and R[]
        for i in range(0 , n1):
            L[i] = arr[l + i]
    
        for j in range(0 , n2):
            R[j] = arr[m + 1 + j]
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def sort(self):
        self.mergesort(self.lst, 0, len(self.lst) - 1)
    
    def mergesort(self, arr, l, r):
        if l < r:
            m = (l+(r-1)) // 2
 
            # Sort first and second halves
            self.mergesort(arr, l, m)
            self.mergesort(arr, m+1, r)
            self._sort(arr, l, m, r)