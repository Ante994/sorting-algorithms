# The ideal sorting algorithm would have the following properties:

# Stable: Equal keys aren’t reordered.
# Operates in place, requiring O(1) extra space.
# Worst-case O(n·lg(n)) key comparisons.
# Worst-case O(n) swaps.
# Adaptive: Speeds up to O(n) when data is nearly sorted or when there are few unique keys.

# There is no algorithm that has all of these properties, and so the choice of sorting algorithm depends on the application.

# merge, quick, insertion, selection, bubble, heap, smooth, shell, radix

from algorithms.merge import SelectionSort
from timeit import default_timer as timer
import random
#start = timer()

lst = SelectionSort(1000) # try with x0, x000, x0000 to mesure sorting time
lst.printElements()
lst.sort()
lst.printElements() 
end = timer()
#print(end - start)
